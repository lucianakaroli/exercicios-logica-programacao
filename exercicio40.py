# Escreva um programa que pergunte o valor inicial de uma divida e o juro mensal. Pergunte tambem
# o valor mensal que sera pago. Imprima o numero de meses pra que a divida seja paga, o total pago
# e o juros pago. 


valor_inicial = float(input("Digite o valor inicial da divida: "))
juro_mensal = float(input("Digite o valor do juro mensal: "))
valor_mensal = float(input("Digite o valor mensal a ser pago: "))  

mes = 1
valor_restante = valor_inicial
juro_total = 0
soma_total = 0

while valor_restante > 0: 
    juros_mes = valor_restante * juro_mensal

    valor_restante = (valor_restante + juros_mes) - valor_mensal
    juro_total = juro_total + juros_mes
    soma_total = soma_total + (juros_mes + valor_mensal)
    mes = mes + 1 

print("Mes total: ", mes)
print("Valor total: ", soma_total)
print("Juros total: ", juro_total)
