# Escreva um produto que leia dois numeros e que pergunte qual operacao voce deseja realizar. 
# Voce deve poder calcular a soma, subtracao, multiplicacao e divisao. Exiba o resultado da operacao solicitada

num1 = float(input("Digite um numero: "))
num2 = float(input("Digite outro numero maior: "))
if num2 < num1:
  print("ERRO. O segundo numero deve ser maior!")
  num2 = float(input("Digite novamente o valor do segundo numero: "))
print("Opcao 1: soma dos numeros.")
print("Opcao 2: subtracao dos numeros.")
print("Opcao 3: multiplicaco dos numeros.")
print("Opcao 4: divisao dos numeros.")
opcao = int(input("Digite uma opcao de 1 a 4: "))
if opcao <1 or opcao > 4:
  print("ERRO. As opcoes sao de 1 a 4!")

if opcao == 1:
    soma = num1 + num2
    print("A soma dos numeros é: ", soma)
else:
    if opcao == 2:
        subtracao = num2 - num1
        print("A subtracao dos numeros é: ", subtracao)
    else:
        if opcao == 3:
            multiplicacao = num1 * num2
            print("A multiplicacao dos numeros é: ", multiplicacao)
        else:
            if opcao == 4:
                divisao = num2 / num1
                print("A divisao dos numeros é: ", divisao)
          