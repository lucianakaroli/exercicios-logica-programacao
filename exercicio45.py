# Escreva um programa que verifique se é ou nao é um numero primo. Para fazer a verificacao,
# calcule o resto da divisao por 2 e depois por todos os numeros impares ate o numero lido.
# Se o resto de uma das divisoes for igual a zero, o numero nao é primo. Observe que 0 e 1 
# nao sao primos e que 2 é o unico numero primo que é par.

num = (int(input("Digite qualquer numero para saber se é primo: ")))

x = 1
while x <= 1:
    if num == 0 or num == 1:
        print("Este numero nao é primo")
    elif num == 2:
        print("Este numero é primo")
    elif num == 3:
        print("Este numero é primo")
    elif num % 2 == 0:
        print("Este numero nao é primo")
    elif num % 3 == 0:
        print("Este numero nao é primo")
    else:
        print("Este numero é primo")
    x = x + 1