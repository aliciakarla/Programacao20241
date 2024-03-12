Valores=  list()
opcao = ' '

while True:
    n = int(input('Digite um valor: '))
    if n not in Valores:
        Valores.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    opcao = str(input('Quer continuar ? [S/N] '))
    if opcao in 'Não':
        break
print('-='*30)
Valores.sort()
print(f'Você digitou os valores {Valores}')