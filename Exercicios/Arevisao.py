nomes = []

while True:
    nome = input("Digite um nome (ou 'FIM' para terminar): ")
    if nome.upper() == "FIM":
        break
    nomes.append(nome)

nomes_filtrados = [nome for nome in nomes if len(nome) > 6]

print("Nomes com mais de 6 letras:")
for nome in nomes_filtrados:
    print(nome)
