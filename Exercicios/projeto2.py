import requests
from bs4 import BeautifulSoup

# URL da página com os dados dos professores
url = "https://diatinf.ifrn.edu.br/docentes/"

# Enviar a requisição para obter o conteúdo da página
response = requests.get(url)
response.raise_for_status()  # Verifica se houve algum erro na requisição

# Parsear o conteúdo HTML com BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Lista para armazenar os dados dos professores
professores = []

# Encontrar todos os blocos que contêm as informações dos professores
for docente in soup.select('.docente'):
    nome = docente.select_one('.nome')
    email = docente.select_one('.email')
    
    if nome and email:
        # Limpar o texto e extrair informações
        nome_texto = nome.get_text(strip=True)
        email_texto = email.get_text(strip=True)
        
        # Adicionar os dados à lista de dicionários
        professores.append({
            'nome': nome_texto,
            'email': email_texto
        })

# Imprimir os dados de nome e email de cada docente
for professor in professores:
    print(f"Nome: {professor['nome']}, Email: {professor['email']}")
