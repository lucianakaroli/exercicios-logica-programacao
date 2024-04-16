# Escreva um programa para aprovar o emprestimo bancario para compra de uma casa. O programa deve perguntar
# o valor da casa a comprar, o salário e a quantidade de anos a pagar. O valor da prestacao mensal nao pode
# ser superior a 30% do salario. Calcule o valor da prestacao como sendo o valor da casa a comprar dividido 
# pelo numero de meses a pagar.

valor_casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o seu salario: "))
qtd_anos_pagar = int(input("Em quantos anos voce deseja pagar a casa?"))
qts_meses_pagar = qtd_anos_pagar*12
valor_prestacao = valor_casa / qts_meses_pagar

if valor_prestacao > salario * 0.3:
    print("Emprestimo bancario nao aprovado, seu salário é inferior!")

else:
    valor_prestacao = valor_casa / qts_meses_pagar
    print("O valor da prestação será de: ", valor_prestacao)