vcasa = str(input('Qual é o valor da casa? R$'))
vsal = str(input('Qual é o seu salário? R$'))
anos = str(input('Em quantos anos você pretende pagar? '))
if float(vsal) * 0.3 > float(vcasa) / (int(anos) * 12):
    mensagem = (' Para pagar uma casa de  R${} em {} anos, '
                'a prestação será de R${:.2f}')
    prestacao = float(vcasa) / (int(anos) * 12)
    print(mensagem.format(vcasa, anos, prestacao),
          ", o valor da prestação é menor que 30% do seu salário. "
          "Empréstimo aprovado!")
else:
    mensagem = (' Para pagar uma casa de  R${} em {} anos, '
                'a prestação será de R${:.2f}')
    prestacao = float(vcasa) / (int(anos) * 12)
    print(mensagem.format(vcasa, anos, prestacao),
          " o valor da prestação é maior que 30% do seu salário. "
          "Empréstimo negado!")