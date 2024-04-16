# Escreva um programa que converta uma temperatura digitada em graus em farenheit. A formula para essa conversao é:
# F = 9 * C/5 +32

graus = float(input("Digite a temperatura em graus: "))
f = (9 * graus / 5) + 32
print("A conversao da temperatura em graus: ", graus " para farenheit é: ", f)
