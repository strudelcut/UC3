import requests

url = "https://randomuser.me/api"
# Fazendo uma requisição GET
response = requests.get(url)
# Exibe o conteúdo json
print(response.json())