import requests
from bs4 import BeautifulSoup

def main():
    Link = 'https://diatinf.ifrn.edu.br/docentes/'
    Response = requests.get(Link)
    Response.raise_for_status()
    print(Response)
    #print(Response.text)

    Site = BeautifulSoup(Response.text, 'html.parser')
    #print(Site.prettify())
    Professores = []

    for Docente in Site.select('.docente'):
        Nome = Docente.select_one('h2') 
        Matricula = Docente.select_one('h2')
        Email = Docente.select_one('a') 

        if Nome and Matricula and Email:
            DadosProfessores= {
                'h2': Nome.get_text(strip=True),
                'h2': Matricula.get_text(strip=True),
                'a': Email.get_text(strip=True)
            }
            Professores.append(DadosProfessores)


    for Professor in Professores:
       print(f"Nome: {Professor['h2']}, Email: {Professor['a']}")

if __name__ == '__main__':
    main()
