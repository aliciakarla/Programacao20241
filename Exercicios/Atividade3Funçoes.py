def MontanteFinal(Montante_Inicial, Juros_Mensais, Meses):    
    Montante_Final = Montante_Inicial * (1 + Juros_Mensais)**Meses    
    return Montante_Final 

ListaDeMeses = [] 

Montante_Inicial = float(input("Digite o montante inicial do investimento: "))
Juros_Mensais = float(input("Digite a taxa de juros mensais: "))
Meses = int(input("Digite a quantidade de meses: "))  

Montante_Final = MontanteFinal(Montante_Inicial, Juros_Mensais, Meses) 

for mes in range(1, Meses + 1):
    ValorAcumulado = Montante_Inicial * (1 + Juros_Mensais)**mes    
    ListaDeMeses.append({"mes": mes, "valor": ValorAcumulado})  
    
print(f"O montante final do investimento após {Meses} meses é: R$ {Montante_Final}\n") 
print("Listagem do mês com o valor acumulado:")
for item in ListaDeMeses:     
    print(f"Mês: {item['mes']} - Valor acumulado: R$ {item['valor']}")
