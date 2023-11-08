import requests
from bs4 import BeautifulSoup
import json

# URL do seu site
url = 'COLOQUE_AQUI_O_LINK_DO_SEU_SITE'

# Realiza uma requisição HTTP para obter o conteúdo da página
response = requests.get(url)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    # Analisa o HTML da página
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Encontre o elemento HTML desejado, por exemplo, usando a classe "tags-item"
    tags_item = soup.find_all("a", class_="tags-item")

    # Crie um dicionário para armazenar os dados
    data = {
        "img": []
    }

    # Itera sobre os elementos encontrados
    for tag in tags_item:
        img_src = tag.find("img")["src"]
        data["img"].append(img_src)

    # Salva os dados em formato JSON
    with open('api.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

    print("Dados coletados e salvos em 'api.json'")
else:
    print("Falha ao fazer a requisição HTTP.")

