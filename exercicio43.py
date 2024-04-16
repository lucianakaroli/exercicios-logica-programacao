# Execute o programa (exercicio 41) para os seguintes valores: 501, 745, 384, 2, 7 e 1.

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
