# Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80km/h, exiba uma mensagem dizendo
# que o usuário foi multado. Neste caso, exiba o valor da multa cobrando R$ 5,00 por km acima de 80. 

velocidade = float(input("Digite a velocidade do carro: "))
if velocidade > 80:
    multa = (velocidade - 80) * 5
    print("Você foi multado! Você deverá pagar: ", multa)
if velocidade <= 80:
    print("Você está dentro da normalidade.")