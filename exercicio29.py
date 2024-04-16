# Modifique um programa para imprimir numeros pares de 0 até um numero digitado
# pelo usuario.

fim = int(input("Digite o ultimo numero a imprimir: "))
num = 0
while num <= fim:
    if num % 2 == 0:
        print(num)
    num = num + 1