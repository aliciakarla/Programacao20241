import requests
from bs4 import BeautifulSoup


def main():
    Site = 'https://diatinf.ifrn.edu.br/docentes/'
    Response = requests.get(Site)
    Response.raise_for_status()

    Soup = BeautifulSoup(Response.text, 'html.parser')
    Professores = []

    for Docente in Soup.select('.docente'):
        Nome = Docente.select_one('.nome') 
        Matricula = Docente.select_one('.matricula')
        Email = Docente.select_one('.email') 

        if Nome and Matricula and Email:
            DadosProfessores= {
                'nome': Nome.get_text(strip=True),
                'matricula': Matricula.get_text(strip=True),
                'email': Email.get_text(strip=True)
            }
            Professores.append(DadosProfessores)


    for Professor in Professores:
        print(f"Nome: {Professor['nome']}, Email: {Professor['email']}")

if __name__ == '__main__':
    main()