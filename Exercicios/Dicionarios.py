Dic1 = {}
Dic2 = {}
Nome, Idade = [], []

while True:
    Nome.append(input('Nome: '))
    Idade.append(float(input('Idade: ')))
    Soma = sum(Idade)
    Media = Soma/len(Idade)

    Continuar = input('Continuar? [S/N]: ').strip().upper()
    while Continuar not in ('S', 'N'):
        Continuar = input('Continuar? [S/N]: ').strip().upper()
    if Continuar == 'N':
        print('Finalizado...')
        break
    import random

print (f'\nPessoas Cadastradas: {len(Nome)}')
print (f'A idade média é: ', Media)
print (f'A pessoa escolhida é: {random.choice(Nome)}')