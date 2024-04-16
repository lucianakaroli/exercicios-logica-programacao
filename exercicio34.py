# Modifique o programa anterior de forma que o usuário também digite o início 
# e o fim da tabuada, em vez de começar com 1 e 10.

tabuada = int(input("Tabuada do: "))
inicio = int(input("Digite o primeiro numero: "))
fim = int(input("Digite o segundo numero: "))

x = inicio
while x <= fim:
    print(x * tabuada)
    x = x + 1