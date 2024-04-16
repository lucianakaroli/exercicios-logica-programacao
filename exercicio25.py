# Escreva um programa que calcule o preco a pagar pelo fornecimento de energia eletrica. Pergunte a quantidade
# de kWh consulmidas e o tipo de instalacao: R para residencias, I para industrias e C para comercios. 
# Calcule o preco a pagar de acordo com a tabela a seguir: 

energia_consulmida = float(input("Digite a quantidade de kWh consulmidas: "))
print("R para residencias.")
print("I para industrias.")
print("C para comercios.")
tipo_instalacao = input("Digite a letra do tipo de instalacao R, I ou C: ")
tipo_instalacao = tipo_instalacao.lower()

if tipo_instalacao == "r":
    if energia_consulmida <= 500:
        preco = energia_consulmida * 0.40
    else:
        preco = energia_consulmida * 0.65

if tipo_instalacao == "i":
    if energia_consulmida <= 5000:
        preco = energia_consulmida * 0.55
    else:
        preco = energia_consulmida * 0.60

if tipo_instalacao == "c":
    if energia_consulmida <= 1000:
        preco = energia_consulmida * 0.55
    else:
        preco = energia_consulmida * 0.60

print("Preco a pagar será R$", preco) 