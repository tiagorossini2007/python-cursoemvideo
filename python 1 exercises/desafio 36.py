v= float(input('Qual o valor da casa? R$'))
sal= float(input('Qual o seu salário? R$'))
ano= int(input('Em quantos anos será sua prestação?'))

p= v/(12*ano)
m = sal *30/100


if p<=m:
    print('não é possível fazer esse empréstimo')

else:
print(' é possível fazer esse empréstimo')