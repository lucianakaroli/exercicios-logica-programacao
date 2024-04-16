# Escreva um programa que leia numeros inteiros do teclado. O programa deve ler 
# os numeros até que o usuario digite 0 (zero). No final da execucao exiba a 
# quantidade de numeros digitados, assim como a soma e a media aritmetica.

 
soma = 0
numeros_digitados = 0


while True:
    num = int(input("Digite um numero inteiro ou digite 0 para sair: "))
    if num == 0:
        break

    if num > 0:
        soma = soma + num
        numeros_digitados = numeros_digitados + 1

print("Quantidade numeros digitados:", numeros_digitados)
print("Soma: ", soma)
print("Media aritmetica: ", soma/numeros_digitados)

