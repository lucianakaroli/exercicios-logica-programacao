# Escreva um programa que leia dois numeros. Imprima a divisao inteira do primeiro pelo segundo, assim como o resto
# da divisao. Utilize apenas os operadores da soma para calcular o resultado. Lembre-se de que podemos entender o
# quociente da divisao de dois numeros como a quantidade de vezes que podemos retirar o divisor do dividendo.
# Logo, 20 ÷ 4 = 5, uma vez que podemos subtrair 4 cinco vezes de 20.

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))



inteiro = 0
resto = 0
x= num1
ultimo_valido = 0

while x >= 0:
    x = x - num2
    
    if x > 0:
        ultimo_valido = x
        inteiro = inteiro + 1
        

print("divisao inteira", inteiro)
print("resto", resto)
