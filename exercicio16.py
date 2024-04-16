# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuario, assim como
# a quantidade de dias pelos quais o carro foi alugado. Calcule o preco a pagar, sabendo que o carro custa R$ 60,00
# por dia e R$ 0,15 por km rodado. 

quantidade_km = float(input("Escreva a quantidade de km percorridos: "))
quantidade_dias = int(float("Escreva a quantidade de dias de uso do carro: "))
preco_dia = 60
preco_km = 0.15
preco_pagar = (quantidade_km * preco_dia) + (quantidade_dias * preco_km)
print("O preco total a pagar sera: ", preco_pagar)