# Exercício 9 - Estrutura de Seleção
# F.U.P que peça o valor de uma compra e aplique um desconto de 10% se for acima de R$ 100,00.

valor_compra = float(input("Digite o valor da compra: R$ "))
if valor_compra > 100:
    desconto = valor_compra * 0.10
    valor_final = valor_compra - desconto
    print(f"Desconto aplicado: R$ {desconto:.2f}")
    print(f"Valor final da compra: R$ {valor_final:.2f}")
else:
    print("Nenhum desconto aplicado.")
    print(f"Valor final da compra: R$ {valor_compra:.2f}")