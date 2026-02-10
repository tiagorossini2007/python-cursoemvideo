sal = float(input('Qual é o salário do funcionário?'))
if sal<=1250:
    nsal= sal+sal*15/100
    print('Seu novo salário é de {}'.format(nsal))

else:
        nsal = sal+sal* 10 / 100
        print('Seu novo salário é de {}'.format(nsal))
