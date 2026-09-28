# Exercício 5 - Estrutura de Seleção
# F.U.P que informe um número e diga se ele é positivo, negativo ou zero.

numero = float(input("Digite um número: "))

if numero > 0:
    print("número positivo.")
elif numero < 0:
    print("número negativo.")
else:
    print("número é zero.")