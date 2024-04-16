# Escreva um programa que pergunte o salario do funcionario e calcule o valor do aumento. Para salarios superiores a 
# R$ 1250,00 calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.

salario = float(input("Digite o valor do salário: "))
if salario > 1250:
    aumento1 = (salario * 0.1) + salario
    novo_salario1 = aumento1
    print("O valor do novo salário é: ", novo_salario1)

if salario <= 1250:
    aumento2 = (salario * 0.15) + salario
    novo_salario2 = aumento2
    print("O valor do novo salário é: ", novo_salario2)