def main():
    Pessoas = []

    while True:
        Nome = input("Digite o nome da pessoa ou END para finalizar: ")
        if Nome == "END":
            break
        Email = input("Digite o email: ")

        Pessoa = [Nome, Email]
        Pessoas.append(Pessoa)

    print("Lista de pessoas:")
    for Pessoa in Pessoas:
        print(f"Nome: {Pessoa[0]}, Email: {Pessoa[1]}")

    NomeArquivo = "ListaGeral.txt"
    with open(NomeArquivo, 'w') as arquivo:
        for Pessoa in Pessoas:
            arquivo.write(f"{Pessoa[0]},{Pessoa[1]}\n")

    print(f"Informações salvas no arquivo '{NomeArquivo}'.")

if __name__ == "__main__":
    main()
