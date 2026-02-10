n = int(input('Digite um número:'))
num1 = n // 1 % 10
num2 = n // 10 % 10
num3 = n // 100 % 10
num4 = n // 1000 % 10
print('Unidade: {}'.format(num1))
print('Dezena: {}'.format(num2))
print('Centena: {}'.format(num3))
print('Milhar: {}'.format(num4))
