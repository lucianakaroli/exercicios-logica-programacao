# Escreva um programa que exiba uma lista de opcoes (menu): adicao, subtracao, divisao, multiplicacao
# e sair. Imprima a tabuada da operacao escolhida. Repita até que a opcao saida seja escolhida. 

print("Menu:")
print("0. Sair")
print("1. Adicao")
print("2. Subtracao")
print("3. Divisao")
print("4. Multiplicacao")

while True:
    num = (int(input("Digite o numero para a opcao desejada: ")))

    if num == 0:
        print("Saindo..")
        break

    tabuada = 1
    while tabuada <= 10:
        numero = 1

        while numero <= 10:
            if num == 4:
                print ("%d x %d = %d" % (tabuada, numero, tabuada * numero))
            elif num == 3:
                print ("%d / %d = %d" % (tabuada, numero, tabuada / numero))
            elif num == 2:
                print ("%d - %d = %d" % (tabuada, numero, tabuada - numero))
            elif num == 1:
                print ("%d + %d = %d" % (tabuada, numero, tabuada + numero))
            numero = numero + 1
        tabuada = tabuada + 1

