from flask import Flask, render_template, request, send_file, make_response
from modules.cluster import process_cluster
from modules.sorteio import process_sorteio
import pandas as pd
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cluster')
def cluster_page():
    # Aqui você redirecionaria para a página de cluster, que ainda será detalhada.
    return render_template('cluster.html')

@app.route('/sorteio')
def sorteio_page():
    # Aqui você redirecionaria para a página de sorteio, que ainda será detalhada.
    return render_template('sorteio.html')

@app.route('/upload_cluster', methods=['POST'])
def upload_cluster():
    file = request.files['file']
    df = process_cluster(file)
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False)
    output.seek(0)
    # Criando a resposta e configurando os cabeçalhos para download do arquivo
    response = make_response(output.getvalue())
    response.headers['Content-Type'] = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    response.headers['Content-Disposition'] = 'attachment; filename=clusterizado.xlsx'
    
    return response

@app.route('/upload_sorteio', methods=['POST'])
def upload_sorteio():
    file = request.files['file']
    df = process_sorteio(file)
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False)
    output.seek(0)
    # Criando a resposta e configurando os cabeçalhos para download do arquivo
    response = make_response(output.getvalue())
    response.headers['Content-Type'] = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    response.headers['Content-Disposition'] = 'attachment; filename=sorteados.xlsx'

    return response

if __name__ == '__main__':
    app.run(debug=True)
