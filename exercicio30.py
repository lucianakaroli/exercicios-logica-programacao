# Modifique o programa anterior para imprimir 1 até o numero digitado pelo
# usuario, mas dessa vez apenas os numeros impares.

fim = int(input("Digite o ultimo numero para impressao: "))
x = 1
while x <= fim:
    if x % 2 == 1:
        print(x)
    x = x + 1
