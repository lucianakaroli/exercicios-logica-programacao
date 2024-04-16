# Escreva um programa que pergunte o deposito inicial e a taxa de juros de uma poupanca. 
# Exiba os valores de mes a mes para os 24 primeiros meses. Escreva o total de ganho com juros no periodo.


deposito_inicial = float(input("Digite o valor do deposito inicial: "))
taxa_juros = float(input("Digite a taxa de juros: "))

x = 1
deposito_total = 0
soma_juros = 0


while x <= 24:
    if deposito_total == 0:
        deposito_total = (deposito_inicial * taxa_juros) + deposito_inicial
    else:
        deposito_total = (deposito_total * taxa_juros) + deposito_total
    
    print("Mes ", x, " valor ", deposito_total)

    x = x + 1

print("Total juros acumulado nos 24 meses:", deposito_total-deposito_inicial)

