# Exercício 10 - Estrutura de Repetição
# F.U.P que peça um número e exiba a tabuada de 1 a 10 desse número.

numero = int(input("Digite um número: "))
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

     