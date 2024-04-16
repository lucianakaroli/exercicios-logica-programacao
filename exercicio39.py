# Altere o programa anterior de forma a perguntar tambem o valor depositado mensalmente. Esse valor será 
# depositado no inicio de cada mes e voce devera considera-lo para para calculo de juros do mes seguinte. 




deposito_inicial = float(input("Digite o valor do deposito inicial: "))
taxa_juros = float(input("Digite a taxa de juros: "))
deposito_mensal = float(input("Digite o valor do deposito mensal: "))

x = 1
deposito_total = 0
soma_juros = 0


while x <= 24:
    if deposito_total == 0:
        deposito_total = (deposito_inicial * taxa_juros) + deposito_inicial
    else:
        deposito_total = ( deposito_total + (deposito_total + deposito_mensal) * taxa_juros) + deposito_mensal
    
    print("Mes ", x, " valor ", deposito_total)

    x = x + 1

print("Total juros acumulado nos 24 meses:", deposito_total-deposito_inicial)

