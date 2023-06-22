import requests
import json

# Dados do JSON que você deseja enviar
data = {
    'chave1': 'valor1',
    'chave2': 'valor2',
    'chave3': 'valor3',
    'chave4': 'valor4',
    'chave5': 'valor5'
}

# URL do servidor Django
url = 'http://localhost:8000/seu_endpoint/'

# Converte o JSON em uma string
json_data = json.dumps(data)

# Define o cabeçalho 'Content-Type' como 'application/json'
headers = {'Content-Type': 'application/json'}

# Envia a solicitação POST com o JSON para o servidor Django
response = requests.post(url, data=json_data, headers=headers)

# Verifica o código de status da resposta
if response.status_code == 200:
    print('JSON enviado com sucesso para o servidor Django!')
else:
    print('Falha ao enviar o JSON para o servidor Django.')