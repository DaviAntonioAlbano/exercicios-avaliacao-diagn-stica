# Exercício 12 - Estrutura de Repetição
#  F.U.P que peça um número e faça uma contagem regressiva até zero.

numero = int(input("Digite um número: "))
for i in range(numero, -1, -1):
    print(i)
    