# Escreva um programa para calcular a reducao do tempo de vida de um fumante. Pergunte a quantidade de cigarros
# fumados por dia e quantos anos ele ja fumou. Considere que um fumante perde 10 minnutos de vida a cada cigarro,
# calcule quantos dias de vida um fumante perdera, exiba o total em dias.

quantidade_cigarros = int(input("Quantos cigarros fumados por dia?"))
anos_fumados = int(input("Por quantos anos você fumou/fuma?"))
min_vida = 10
perda_dia = quantidade_cigarros * min_vida
perda_total = perda_dia * 365
perda_total_dias = perda_total * anos_fumados
print("A perda total em dias foi: ", perda_total_dias)






