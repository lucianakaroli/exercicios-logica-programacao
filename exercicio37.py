# Modifique o programa da listagem 5.10 para que aceite respostas com letras minusculas e maiusculas em todas as questoes.

pontos = 0
questao = 1

while questao <= 3:
    resposta = input("Resposta da questao %d: " % questao)
    if questao == 1 and resposta == "b" or resposta == "B":
        pontos = pontos + 1
    if questao == 2 and resposta == "a" or resposta == "A":
        pontos = pontos + 1
    if questao == 3 and resposta == "d" or resposta == "D":
        pontos = pontos + 1
    questao += 1
print ("O aluno fez %d ponto(s)" % pontos)
