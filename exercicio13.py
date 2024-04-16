# Faca um programa que solicite o preco de uma mercadoria e o percentual de desconto. 
# Exiba o valor do desconto e o preco a pagar.

preco_mercadoria = float(input("Digite o valor da mercadoria: "))
desconto = float(input("Digite o percentual de desconto: "))
valor_desconto =  preco_mercadoria * desconto / 100
preco_pagar = preco_mercadoria - valor_desconto

print("O valor do desconto foi de: ", valor_desconto)
print("O preco total a pagar sera de: ",preco_pagar)