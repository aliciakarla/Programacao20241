import requests
from bs4 import BeautifulSoup

Link = "https://diatinf.ifrn.edu.br/docentes/"
Requisicao = requests.get(Link)

print(Requisicao)
#print(Requisicao.text)

Site = BeautifulSoup(Requisicao.text, "html.parser")
#print(Site.prettify())