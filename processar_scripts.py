import pandas as pd
import simplekml
import random
from shapely.geometry import MultiPoint, mapping
from geopy.distance import geodesic

def match_vivo_to_tim_clusters(input_file, output_file):
    df = pd.read_excel(input_file)
    df.columns = [col.strip().upper() for col in df.columns]

    tim_sites = df[df['OPERATOR'] == 'TIM'].copy()
    vivo_sites = df[df['OPERATOR'] == 'VIVO'].copy()

    cluster_centers = tim_sites.groupby('CLUSTER')[['LATITUDE', 'LONGITUDE']].mean().reset_index()
    cluster_centers.rename(columns={'LATITUDE': 'LATITUDE_CLUSTER', 'LONGITUDE': 'LONGITUDE_CLUSTER'}, inplace=True)

    tim_sites = tim_sites.merge(cluster_centers, on='CLUSTER', how='left')

    results = []
    for _, site in vivo_sites.iterrows():
        lat = float(site['LATITUDE'])
        lon = float(site['LONGITUDE'])
        site_coords = (lat, lon)

        uf_clusters = tim_sites[tim_sites['UF'] == site['UF']]['CLUSTER'].unique()
        filtered_centers = cluster_centers[cluster_centers['CLUSTER'].isin(uf_clusters)]

        min_distance = float('inf')
        nearest_cluster = None
        nearest_lat = None
        nearest_lon = None

        for _, row in filtered_centers.iterrows():
            cluster_coords = (row['LATITUDE_CLUSTER'], row['LONGITUDE_CLUSTER'])
            distance = geodesic(site_coords, cluster_coords).km
            if distance < min_distance:
                min_distance = distance
                nearest_cluster = row['CLUSTER']
                nearest_lat = row['LATITUDE_CLUSTER']
                nearest_lon = row['LONGITUDE_CLUSTER']

        if nearest_cluster:
            results.append({
                'STATION_ID': site['STATION_ID'],
                'OPERATOR': 'VIVO',
                'LATITUDE': lat,
                'LONGITUDE': lon,
                'CLUSTER': nearest_cluster,
                'LATITUDE_CLUSTER': nearest_lat,
                'LONGITUDE_CLUSTER': nearest_lon,
                'KM': min_distance,
                'TSK': 0,
                'CIDADE': site.get('CIDADE', ''),
                'UF': site['UF']
            })

    for _, site in tim_sites.iterrows():
        site_coords = (float(site['LATITUDE']), float(site['LONGITUDE']))
        cluster_data = cluster_centers[cluster_centers['CLUSTER'] == site['CLUSTER']].iloc[0]
        cluster_coords = (float(cluster_data['LATITUDE_CLUSTER']), float(cluster_data['LONGITUDE_CLUSTER']))
        distance = geodesic(site_coords, cluster_coords).km

        results.append({
            'STATION_ID': site['STATION_ID'],
            'OPERATOR': 'TIM',
            'LATITUDE': site['LATITUDE'],
            'LONGITUDE': site['LONGITUDE'],
            'CLUSTER': site['CLUSTER'],
            'LATITUDE_CLUSTER': cluster_data['LATITUDE_CLUSTER'],
            'LONGITUDE_CLUSTER': cluster_data['LONGITUDE_CLUSTER'],
            'KM': distance,
            'TSK': site.get('TSK', 0),
            'CIDADE': site.get('CIDADE', ''),
            'UF': site['UF']
        })

    df_result = pd.DataFrame(results)
    df_result.to_excel(output_file, index=False)
    return output_file

def gerar_kml(input_file, output_file):
    df = pd.read_excel(input_file)
    unique_clusters = df['CLUSTER'].unique()
    cluster_colors = { cluster: generate_pastel_color() for cluster in unique_clusters }

    kml = simplekml.Kml()

    for uf in df['UF'].unique():
        uf_folder = kml.newfolder(name=uf)
        clusters_uf = df[df['UF'] == uf].groupby('CLUSTER')

        for cluster, cluster_data in clusters_uf:
            cluster_folder = uf_folder.newfolder(name=cluster)
            color_hex = cluster_colors[cluster]
            poly_color = f"88{color_hex}"

            points = [(lon, lat) for lon, lat in zip(cluster_data['LONGITUDE'], cluster_data['LATITUDE'])]
            if len(points) >= 3:
                cluster_polygon = MultiPoint(points).convex_hull
                coords = list(mapping(cluster_polygon)['coordinates'][0])
            else:
                coords = points

            tsk_total = cluster_data['TSK'].sum()
            tsk_mensal = round(tsk_total / 4, 2)

            cluster_remark = f"""
            <![CDATA[
            <b>Cluster:</b> {cluster}<br/>
            <b>UF:</b> {uf}<br/>
            <b>Sites TIM:</b> {len(cluster_data[cluster_data['OPERATOR'] == 'TIM'])}<br/>
            <b>Sites VIVO:</b> {len(cluster_data[cluster_data['OPERATOR'] == 'VIVO'])}<br/>
            <b>TSK Total:</b> {tsk_total}<br/>
            <b>TSK Médio por mês:</b> {tsk_mensal}<br/>
            <b>Cidades:</b><br/>
            """
            cidades = cluster_data.groupby('CIDADE').size().to_dict()
            for cidade, count in cidades.items():
                cluster_remark += f"- {cidade}: {count}<br/>"
            cluster_remark += "]]>"

            pol = cluster_folder.newpolygon(name=cluster)
            pol.outerboundaryis = coords
            pol.style.polystyle.color = poly_color
            pol.style.polystyle.outline = 1
            pol.description = cluster_remark

            first_lat = cluster_data.iloc[0]['LATITUDE_CLUSTER']
            first_lon = cluster_data.iloc[0]['LONGITUDE_CLUSTER']

            cluster_icon = cluster_folder.newpoint(name=cluster)
            cluster_icon.coords = [(first_lon, first_lat)]
            cluster_icon.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/star.png'
            cluster_icon.style.iconstyle.color = 'ff00ffff'
            cluster_icon.style.iconstyle.scale = 2.0
            cluster_icon.description = cluster_remark

            for _, site in cluster_data.iterrows():
                pt = cluster_folder.newpoint()
                pt.coords = [(site['LONGITUDE'], site['LATITUDE'])]
                icon_url = 'http://maps.google.com/mapfiles/kml/shapes/triangle.png' if site['OPERATOR'] == 'VIVO' else 'http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png'
                pt.style.iconstyle.icon.href = icon_url
                pt.style.iconstyle.color = f"ff{color_hex}"
                pt.style.iconstyle.scale = 0.8
                pt.name = ''

                site_coords = (site['LATITUDE'], site['LONGITUDE'])
                cluster_coords = (first_lat, first_lon)
                distance = geodesic(site_coords, cluster_coords).km

                pt.description = f"""
                <![CDATA[
                <b>Station_ID:</b> {site['STATION_ID']}<br/>
                <b>UF:</b> {uf}<br/>
                <b>Distância ao Cluster:</b> {distance:.2f} km<br/>
                <b>Operador:</b> {site['OPERATOR']}<br/>
                <b>Cluster:</b> {site['CLUSTER']}
                ]]>
                """

    kml.save(output_file)
    return output_file

def generate_pastel_color():
    r = random.randint(100, 255)
    g = random.randint(100, 255)
    b = random.randint(100, 255)
    return f"{b:02x}{g:02x}{r:02x}"
