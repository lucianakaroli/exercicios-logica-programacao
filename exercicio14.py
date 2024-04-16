# Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distancia a percorrer e a velocidade
# media esperada para a viagem

distancia = float(input("Digite o valor da distancia: "))
velocidade_media = float(input("Digite a velocidade media: "))
tempo = distancia / velocidade_media

print("O tempo total da viagem de carro foi de: ",tempo)