import requests
from bs4 import BeautifulSoup

# URL da página com os dados dos professores
url = 'https://diatinf.ifrn.edu.br/docentes/'

# Função principal para capturar e processar os dados
def main():
    # Fazer a requisição HTTP para obter o conteúdo da página
    response = requests.get(url)
    response.raise_for_status()  # Verifica se houve algum erro na requisição

    # Analisar o conteúdo HTML com BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Lista para armazenar os dados dos professores
    professores = []

    # Encontrar todas as seções que contêm os dados dos professores
    # Ajuste os seletores conforme necessário dependendo da estrutura HTML da página
    for docente in soup.select('.docente'):  # Ajuste o seletor conforme necessário
        nome = docente.select_one('.nome')  # Ajuste o seletor conforme necessário
        matricula = docente.select_one('.matricula')  # Ajuste o seletor conforme necessário
        email = docente.select_one('.email')  # Ajuste o seletor conforme necessário

        if nome and matricula and email:
            dados_docente = {
                'nome': nome.get_text(strip=True),
                'matricula': matricula.get_text(strip=True),
                'email': email.get_text(strip=True)
            }
            professores.append(dados_docente)

    # Imprimir os nomes e e-mails dos professores
    for professor in professores:
        print(f"Nome: {professor['nome']}, Email: {professor['email']}")

if __name__ == '__main__':
    main()
