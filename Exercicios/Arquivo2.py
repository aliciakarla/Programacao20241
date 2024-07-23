def LerArquivo(NomeArquivo):
    Pessoas = []

    with open(NomeArquivo, 'r') as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if linha:
                nome, email = linha.split(',')
                Pessoas.append([nome, email])
    return Pessoas

def main():
    NomeArquivo = "ListaGeral.txt"
    PessoasRestauradas = LerArquivo(NomeArquivo)

    print("Informações restauradas do arquivo:")
    for pessoa in PessoasRestauradas:
        print(f"Nome: {pessoa[0]}, Email: {pessoa[1]}")

if __name__ == "__main__":
    main()
