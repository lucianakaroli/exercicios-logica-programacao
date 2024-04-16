# Escreva um programa que pergunte a distancia que um passageiro deseja percorrer em km. Calcule o preco
# da passagem, cobrando R$ 0,50 por km para viagens de até 200km e R$ 0,45 para viagens mais longas.

distancia = float(input("Digite a distancia da viagem em km: "))

if distancia <=200:
    preco_passagem1 = distancia * 0.5
    print("O preco da passagem será: ", preco_passagem1)

else:
    preco_passagem2 = distancia * 0.45
    print("O preco da passagem será: ", preco_passagem2)