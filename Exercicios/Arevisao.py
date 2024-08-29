ListaDeNomes = [] 

while True:
    Nomes = input("Digite um nome: ")

    Continuar = input('Continuar? [S/N]: ').strip().upper()
    while Continuar not in ('S', 'N'):
        Continuar = input('Continuar? [S/N]: ').strip().upper()
    if Continuar == 'N':
        print('Fim...')
        break
    import random



