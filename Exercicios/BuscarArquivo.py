import os
import sys

def BuscarArquivo(NomeDoArquivo, Pasta):
    CaminhosEncontrados = []
    for raiz, dirs, arquivos in os.walk(Pasta):
        if NomeDoArquivo in arquivos:
            CaminhoAbsoluto = os.path.join(raiz, NomeDoArquivo)
            CaminhosEncontrados.append(os.path.abspath(CaminhoAbsoluto))
    return CaminhosEncontrados

def main():
    if len(sys.argv) != 3:
        print("Uso: python buscar_arquivo.py <nome_arquivo> <pasta>")
        sys.exit(1)
    NomeDoArquivo = sys.argv[1]
    Pasta = sys.argv[2]

    if not os.path.isdir(Pasta):
        print(f"A pasta '{Pasta}' não existe.")
        sys.exit(1)
    Caminhos = BuscarArquivo(NomeDoArquivo, Pasta)

    if Caminhos:
        print("Arquivos encontrados:")
        for Caminho in Caminhos:
            print(Caminho)
    else:
        print("Nenhum arquivo encontrado.")

if __name__ == "__main__":
    main()
