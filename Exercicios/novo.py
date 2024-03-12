x = int(input('Entre um número inteiro: '))
f = x // 2
while f > 1:
    if x % f == 0:
       print(x, ' tem fator ', f)
       break
    f = f - 1
else:
    print(x, ' é um número primo!')