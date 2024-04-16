# Escreva um programa que leia dois números. Imprima o resultado da multiplicação 
# do primeiro pelo segundo. Utilize apenas os operadores de soma e subtração para
# calcular o resultado. Lembre-se de que podemos entender a multiplicação de dois 
# números como somas sucessivas de um deles.
# Assim, 4 × 5 = 5 + 5 + 5 + 5 

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

tabuada = 0 
x = 1

while x <= num1: 
    tabuada = tabuada + num2
    x = x + 1

print(tabuada)