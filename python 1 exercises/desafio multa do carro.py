v = float(input('Qual foi a velocidade do carro?'))
if v > 80:
    print('Você foi multado,')
    m = (v-80) * 7
    print('Sera necessário pagar uma multa de R${}'.format(m))

else:
    print('Você nao foi multado!')


