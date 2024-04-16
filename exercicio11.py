# Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos

dias = int(input("Digite um dia: "))
horas = int(input("Digite a hora: "))
minutos = int(input("Digite os minutos"))
segundos = int(input("Digite os segundos"))

total_em_segundos = dias*86400 + horas*3600 + minutos*60 + segundos
print("Convertidos em segundos, o valor total é: ", total_em_segundos)