preco = int(input("Digite o valor do produto: R$"))
print("Formas de pagamento:")
print("1 - À vista dinheiro/cheque")
print("2 - À vista cartão")
print("3 - 2x no cartão")
print("4 - 3x ou mais no cartão")
print("Digite a opção de pagamento:")
opcao = int(input())
if opcao == 1:
    desconto = preco * 0.10
    valor_final = preco - desconto
    print(f"Parabéns, vocé recebeu um desconto de "
          f"R${desconto:.2f}. Valor final: R${valor_final:.2f}")
elif opcao == 2:
    desconto = preco * 0.05
    valor_final = preco - desconto
    print(f"Parabéns, vocé recebeu um desconto de "
          f"R${desconto:.2f}. Valor final: R${valor_final:.2f}")
elif opcao == 3:
    valor_final = preco
    print(f"Valor final: R${valor_final:.2f}.")
elif opcao == 4:
    juros = preco * 0.20
    valor_final = preco + juros
    print(f"Vocé recebeu um juros de R${juros:.2f}. "
          f"Valor final: R${valor_final:.2f}.")