#Faca um programa que calcule o aumento de um salario. Ele deve solicitar o valor do salario e a porcentagem
#do aumento. Exiba o valor do aumento e do novo salario.

salario = float(input("Digite o valor do salario: "))
aumento = float(input("Digite o valor do aumento em porcentagem: "))
novo_salario = (salario + (salario * aumento / 100))
print("O aumento do salário foi: ",novo_salario)
