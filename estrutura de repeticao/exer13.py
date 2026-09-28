# Exercício 13 - Estrutura de Repetição
# F.U.P que gere um número aleatório de 1 a 100 e peça ao usuário para adivinhar, dando dicas de "maior" ou "menor" até acertar. 

import random

numero_secreto = random.randint(1, 100)
tentativas = 0

while True:
    palpite = int(input("Tente adivinhar o número (1-100): "))
    tentativas += 1

    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        break
    elif palpite < numero_secreto:
        print("O número é maior.")
    else:
        print("O número é menor.")
        