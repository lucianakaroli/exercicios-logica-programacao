# Escreva um programa para controlar uma pequena maquina registradora. Voce deve solicitar
# ao usuario que digite o codigo do produto e a quantidade comprada. Utilize a tabela de 
# codigos abaixo para obter o preco de cada produto.
# Seu programa deve exibir o total de compras depois que o usuario digitar 0. 
# Qualquer outro codigo deve gerar a mensagem de erro "Codigo invalido". 

preco = 0
total_compra = 0
while True:
    print("Para sair digite 0")
    codigo = int(input("Digite o codigo do produto(1,2,3,5 ou 9): "))
    quantidade = int(input("Digite a quantidade comprada: "))
    if codigo == 0 or quantidade == 0:
        break
    elif codigo != 1 and codigo != 2 and codigo != 3 and codigo != 5 and codigo != 9:
        print("Codigo invalido.")
    elif codigo == 1:
        preco = 0.50
    elif codigo == 2:
        preco = 1.00
    elif codigo == 3:
        preco = 4.00
    elif codigo == 5:
        preco = 7.00
    elif codigo == 9:
        preco = 8.00
    total_compra = total_compra + (preco * quantidade)
                            
print("Total de compras: ", total_compra)
