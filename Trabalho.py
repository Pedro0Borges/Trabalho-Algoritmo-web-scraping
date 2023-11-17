import requests
from bs4 import BeautifulSoup

# URL da página que você deseja fazer scraping
url = 'https://tribunademinas.com.br/noticias/politica'

# Realiza a requisição HTTP para obter o conteúdo da página
response = requests.get(url)

html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

noticia = soup.find_all("h2" , class_ = "title")

for k in noticia:
    print(k.text)





