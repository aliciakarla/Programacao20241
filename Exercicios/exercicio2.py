print("Valor mínimo do saque: R$10,00.")
print("Valor máximo do saque: R$1000,00")
saque = int(input("Valor do saque: R$"))

while(saque<10) or (saque>1000):
  print("Valor fora dos limites.")
saque = int(input("Digite novamente: R$"))

if(saque>=10) and (saque<=1000):
    resto1 = saque % 100
    resto2 = resto1 % 50
    resto3 = resto2 % 20
    resto4 = resto3 % 10
    resto5 = resto4 % 5
    resto6 = resto5 % 1
    nota100,nota50,nota20,nota10,nota5, = saque//100,resto1//50,resto2//20,resto3//10,resto4//5,resto5//1,resto6

print("R$100,00:",nota100)
print("R50,00:",nota50)
print("R$20,00:",nota20)
print("R$10,00:",nota10)
print("R$5,00:",nota5)
