# TIM Field Simulation

Esta aplicação utiliza Streamlit para simular o deslocamento de técnicos de campo (FME) até diferentes sites.

## Como executar localmente

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
2. Rode o aplicativo a partir do diretório do projeto (ou forneça o caminho
   completo do arquivo):
   ```bash
   streamlit run tim_field_sim.py
   ```

Caso nenhum arquivo CSV seja carregado pela interface, serão utilizados os arquivos presentes no repositório (`Tickets.csv`, `FME.csv`, `CM.csv`, `Site.csv`).
Esses arquivos são buscados automaticamente no mesmo diretório do script,
permitindo executar o comando de qualquer pasta.

## Implantação no Streamlit Cloud

Basta criar um repositório contendo este código e definir `tim_field_sim.py` como arquivo principal. Inclua também o arquivo `requirements.txt`.
