from random import randint
from time import sleep
c = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5, tente adivinhar')
print('-=-' * 20)
j = int(input('em que número eu pensei?'))
print('PROCESSANDO')
sleep(3)
if j == c:
    print('Parabéns, você acertou')

else:
    print('Você errou')

