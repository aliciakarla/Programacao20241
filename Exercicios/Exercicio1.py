from datetime import datetime
from time import sleep


Cedulas = ('R$100', 'R$50', 'R$20', 'R$10', 'R$5')
n = (100, 50, 20, 10, 5)
ced = list()
ced1 = list()
frase1 = list()
num = list()
rest = list()
valor1 = 0

for X in range(0, len(n)):
    frase1.append(Cedulas[X])
    ced.append(0)
    ced1.append(0)
    num.append(0)
    rest.append(0)

for X in range(0, len(n)):
    while True:
        opc = input('Informe o número de cédulas de {}: '.format(Cedulas[X]))
        if opc.isnumeric():
            opc = int(opc)
            break
        else:
            print('NÃO É UM VALOR!')

    ced[X] = opc
    valor1 += ced[X] * n[X]

print('\nSALDO DISPONÍVEL NO CAIXA ELETRÔNICO R${:.2f}'.format(valor1))
while True:
    hora = datetime.today().hour
    opc = ' '

    for c in range(0, len(n)):
        if ced[c] > 0:
            frase1[c] = [c]
            frase1[c] = Cedulas [c]
        else:
            frase1[c] = ''

    for c in range(0, len(n)):
        ced1[c] = ced[c]
        num[c] = 0

    print('\n' + '----------------------------' * 2)
    print(' ' * 17 + 'CAIXA ELETRÔNICO')
    print('NOTAS DISPONÍVEIS: ', end='')
    for c in range(0, len(n)):
        print('{}'.format(frase1[c]), end=' ')
    print('\n' + '----------------------------' * 2)

    while True:
        valor = input('SAQUE R$: ')
        if valor.isnumeric():
            valor = int(valor)
            break
        else:
            print('NÃO É POSSIVEL ATENDER AO PEDIDO!')

    if valor1 >= valor and valor1 > 0:
        for c in range(0, len(n) - 1):

            if ced1[c] > 0:
                num[c] = valor // n[c]
                rest[c] = valor % n[c]

                if num[c] < ced1[c]:
                    ced1[c] -= num[c]
                    valor = rest[c]
                else:
                    num[c] = ced1[c]
                    valor -= ced1[c] * n[c]
                    ced1[c] = 0

        if ced1[len(n) - 1] > 0:
            if valor <= ced1[len(n) - 1]:
                num[len(n) - 1] = valor
                rest[len(n) - 1] = 0
                ced1[len(n) - 1] -= num[len(n) - 1]
                valor1 = 0

                for c in range(0, len(n)):
                    ced[c] = ced1[c]
                    valor1 += ced1[c] * n[c]

                print('----------------------------')
                print('SAQUE REALIZADO COM SUCESSO!')
                print('\nCONTANDO CÉDULAS...\n')
                sleep(2)
                for d in range(0, len(n)):
                    print('CÉDULAS DE {}: {}'.format(Cedulas[d], num[d]))
                print('----------------------------')
                
                break
