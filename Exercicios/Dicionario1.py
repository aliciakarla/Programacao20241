from pprint import pprint
Lista = []

for i in range (4):
    ano = int(input('Digite o ano: '))
    bissexto = False
    if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:  
        bissexto = True
    Lista.append({"Ano": ano, "Bissexto": bissexto})

pprint (Lista)
