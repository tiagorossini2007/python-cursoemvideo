n = float(input('Qual foi a distância percorrida:'))
if n<=200:
    v = (n/2)
    print('Você está prestes a começar uma viagem de {}km, será necessário pagar {} reais '.format(n,v))

else:
    v = (n*0.45)
    print('Você está prestes a começar uma viagem de {}km, será necessário pagar {} reais '.format(n, v))





