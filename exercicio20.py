# Escreva um programa que leia tres numeros e que imprima o maior e o menor

a = float(input("Digite um numero: "))
b = float(input("Digite outro valor: "))
c = float(input("Digite outro valor: "))

if a > b and a > c:
    print("O maior valor é: ", a)
if b > a and b > c:
    print("O maior valor é: ", b)
if c > a and c > b:
    print("O maior valor é: ", c)

if a < b and a < c:
    print("O menor valor é: ", a)
if b < a and b < c:
    print("O menor valor é: ", b)
if c < a and c < b:
    print("O menor valor é: ", c)