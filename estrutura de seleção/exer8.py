# Exercício 8 - Estrutura de Seleção
# F.U.P que informe a idade de uma pessoa e classifique-a como criança (0-12), adolescente (13-17) ou adulto (18+).

idade = int(input("Digite a idade da pessoa: "))
if idade >= 0 and idade <= 12:
    print("Criança.")
elif idade >= 13 and idade <= 17:
    print("Adolescente.")
else:
    print("Adulto.")
