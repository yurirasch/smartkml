from flask import Flask, request, render_template, send_from_directory
import os
from processar_scripts import match_vivo_to_tim_clusters, gerar_kml

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
RESULT_FOLDER = 'resultados'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        f = request.files['file']
        filepath = os.path.join(UPLOAD_FOLDER, f.filename)
        f.save(filepath)

        output_excel = os.path.join(RESULT_FOLDER, 'resultado.xlsx')
        output_kml = os.path.join(RESULT_FOLDER, 'resultado.kml')

        match_vivo_to_tim_clusters(filepath, output_excel)
        gerar_kml(output_excel, output_kml)

        return render_template('resultado.html', excel='resultado.xlsx', kml='resultado.kml')

    return render_template('index.html')

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(RESULT_FOLDER, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
