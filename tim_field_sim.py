import pandas as pd
import simpy
from datetime import datetime, timedelta
import streamlit as st
from streamlit_folium import st_folium
import folium
from folium.plugins import TimestampedGeoJson
import requests

GRAPH_URL = "http://localhost:8989/route"

# Função para calcular distância da rota (com fallback snap)
def route_distance(lat1, lon1, lat2, lon2):
    for delta in [0, 0.05, -0.05, 0.1, -0.1]:
        try:
            p1 = f"{lat1},{lon1}"
            p2 = f"{lat2+delta},{lon2+delta}"
            resp = requests.get(GRAPH_URL, params={
                "point": [p1, p2],
                "profile": "car",
                "locale": "en",
                "calc_points": "false"
            }, timeout=10)
            if resp.status_code == 200:
                data = resp.json()
                if "paths" in data and data["paths"]:
                    return data["paths"][0]["distance"] / 1000  # em km
        except:
            pass
    return None

# Simulação
class FieldSimulation:
    def __init__(self, env, tickets, techs, sites, cms, speed=60, max_tickets=None):
        self.env = env
        self.tickets = tickets.head(max_tickets) if max_tickets else tickets
        self.techs = techs
        self.sites = sites
        self.cms = cms
        self.speed = speed
        self.map_points = []
        self.cm_status = {cm: {"available": list(techs[techs["CM"] == cm]["FME"])} for cm in cms["CM"].unique()}

    def run(self):
        for _, ticket in self.tickets.iterrows():
            # Pega o CM do site
            site_row = self.sites[self.sites["SITE"] == ticket["SITE"]]
            if site_row.empty:
                print(f"[IGNORADO] SITE={ticket['SITE']} - site não encontrado")
                continue
            site = site_row.iloc[0]
            cm = site["CM"]
            available = self.cm_status.get(cm, {"available": []})["available"]
            if not available:
                print(f"[IGNORADO] Nenhum técnico disponível no CM: {cm} para SITE={ticket['SITE']}")
                continue
            fme = available.pop(0)
            self.env.process(self.dispatch(fme, cm, site, ticket))
        self.env.run()

    def dispatch(self, fme, cm, site, ticket):
        cm_row = self.cms[self.cms["CM"] == cm]
        if cm_row.empty:
            # fallback: pega média dos sites do CM
            cm_sites = self.sites[self.sites["CM"] == cm]
            if cm_sites.empty:
                print(f"[IGNORADO] CM {cm} sem localização!")
                return
            cm_lat = cm_sites["LAT"].astype(float).mean()
            cm_lon = cm_sites["LON"].astype(float).mean()
        else:
            cm_lat = float(cm_row.iloc[0]["LAT"])
            cm_lon = float(cm_row.iloc[0]["LON"])

        site_lat, site_lon = float(site["LAT"]), float(site["LON"])
        ts_ini = start_dt + timedelta(seconds=self.env.now * self.speed)
        self.add_marker(ts_ini, cm_lat, cm_lon, f"FME: {fme}<br>Status: Disponível<br>CM: {cm}", "home", "green", 1)

        # Espera até o momento do ticket
        yield self.env.timeout((ticket["DATA/TIME"] - start_dt).total_seconds() / self.speed)

        # Vai de carro até o site
        dist = route_distance(cm_lat, cm_lon, site_lat, site_lon)
        if dist is None:
            print(f"[ERRO ROTA] CM {cm} até {site['SITE']}")
            self.cm_status[cm]["available"].append(fme)
            return
        travel_time = dist / 50  # 50km/h
        atendimento_min = 10

        ts_saida = start_dt + timedelta(seconds=self.env.now * self.speed)
        self.add_marker(ts_saida, cm_lat, cm_lon, f"FME: {fme}<br>Status: Indo para {site['SITE']}<br>Dist: {dist:.1f}km", "car", "blue", 2)

        yield self.env.timeout(travel_time * 3600 / self.speed)

        ts_chegou = start_dt + timedelta(seconds=self.env.now * self.speed)
        self.add_marker(ts_chegou, site_lat, site_lon, f"FME: {fme}<br>Status: Atendendo {site['SITE']}<br>Tempo estimado: {atendimento_min} min", "user", "red", 3)

        yield self.env.timeout(atendimento_min * 60 / self.speed)

        ts_volta = start_dt + timedelta(seconds=self.env.now * self.speed)
        self.add_marker(ts_volta, site_lat, site_lon, f"FME: {fme}<br>Status: Voltando ao CM {cm}", "car", "orange", 2)
        yield self.env.timeout(travel_time * 3600 / self.speed)

        ts_fim = start_dt + timedelta(seconds=self.env.now * self.speed)
        self.add_marker(ts_fim, cm_lat, cm_lon, f"FME: {fme}<br>Status: Disponível<br>CM: {cm}", "home", "green", 1)
        self.cm_status[cm]["available"].append(fme)

    def add_marker(self, ts, lat, lon, popup, icon, color, step):
        self.map_points.append({
            "time": ts,
            "lat": lat,
            "lon": lon,
            "popup": popup,
            "icon": icon,
            "color": color,
            "step": step
        })

def make_map(points, cms, sites, current_time):
    m = folium.Map(location=[-15, -50], zoom_start=5, tiles="CartoDB dark_matter")

    # CM casas verdes
    for _, row in cms.iterrows():
        folium.Marker(
            location=[row["LAT"], row["LON"]],
            popup=f"CM: {row['CM']}",
            icon=folium.Icon(icon="home", prefix="fa", color="green")
        ).add_to(m)

    # Sites (antena laranja)
    for _, row in sites.iterrows():
        folium.Marker(
            location=[row["LAT"], row["LON"]],
            popup=f"SITE: {row['SITE']}",
            icon=folium.Icon(icon="signal", prefix="fa", color="orange")
        ).add_to(m)

    # Técnicos
    for pt in points:
        if pt["time"] <= current_time:
            folium.Marker(
                location=[pt["lat"], pt["lon"]],
                popup=pt["popup"],
                icon=folium.Icon(icon=pt["icon"], prefix="fa", color=pt["color"])
            ).add_to(m)

    return m

# ------------------- STREAMLIT APP -------------------
st.set_page_config(layout="wide")
st.title("Simulação Operacional de Técnicos de Campo (FME)")

with st.sidebar:
    st.header("Parâmetros da Simulação")
    start_str = st.text_input("Data/hora início", "2024-01-01 00:00:00")
    end_str = st.text_input("Data/hora fim", "2024-01-01 03:59:59")
    speed = st.slider("Velocidade (segundos simulados por segundo real)", 10, 3600, 60, 10)
    max_tickets = st.number_input("Máximo de tickets simulados", 1, 1000, 50)

    st.markdown("**Arquivos CSV necessários:**")
    st.markdown("- `Tickets.csv` (DATA/TIME, SITE ...)")
    st.markdown("- `FME.csv` (FME, CM ...)")
    st.markdown("- `CM.csv` (CM, LAT, LON ...)")
    st.markdown("- `Site.csv` (SITE, LAT, LON, CM ...)")

start_dt = datetime.fromisoformat(start_str)
end_dt = datetime.fromisoformat(end_str)

# Lê arquivos
tickets = pd.read_csv("Tickets.csv", encoding="latin1")
tickets["DATA/TIME"] = pd.to_datetime(tickets["DATA/TIME"])
tickets["SITE"] = tickets["SITE"].astype(str).str.strip().str.upper()
tickets = tickets[(tickets["DATA/TIME"] >= start_dt) & (tickets["DATA/TIME"] <= end_dt)].head(max_tickets)

techs = pd.read_csv("FME.csv", encoding="latin1")
cms = pd.read_csv("CM.csv", encoding="latin1")
sites = pd.read_csv("Site.csv", encoding="latin1")
sites["SITE"] = sites["SITE"].astype(str).str.strip().str.upper()
sites["CM"] = sites["CM"].astype(str).str.strip().str.upper()
cms["CM"] = cms["CM"].astype(str).str.strip().str.upper()
techs["CM"] = techs["CM"].astype(str).str.strip().str.upper()

# Roda simulação (cache pra não ficar lento)
@st.cache_data(show_spinner=True)
def run_sim(tickets, techs, sites, cms, speed, max_tickets):
    env = simpy.Environment()
    sim = FieldSimulation(env, tickets, techs, sites, cms, speed, max_tickets)
    sim.run()
    return sim.map_points

st.success(f"Tickets selecionados para simulação: {len(tickets)}")

if len(tickets) == 0:
    st.warning("Nenhum ticket válido no período.")
    st.stop()

points = run_sim(tickets, techs, sites, cms, speed, max_tickets)
if len(points) == 0:
    st.error("Nada a simular. Verifique arquivos.")
    st.stop()

# Cria lista de timestamps únicos ordenados
all_times = sorted(set(pt["time"] for pt in points))
min_time, max_time = all_times[0], all_times[-1]

# Barra de tempo
selected_time = st.slider("Progresso da Simulação", min_value=min_time, max_value=max_time, value=min_time, format="YYYY-MM-DD HH:mm:ss")

# Mostra mapa animado
m = make_map(points, cms, sites, selected_time)
st_folium(m, width=1200, height=700)

# Resumo
st.info(f"Momento selecionado: {selected_time}")
