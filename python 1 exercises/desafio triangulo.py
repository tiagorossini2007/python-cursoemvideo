print('Adivinhando triângulos')
print('-=-' * 20)
r1 = float(input('primeiro segmento:'))
r2 = float(input('segundo segmento:'))
r3 = float(input('terceiro segmento:'))
if r1< r2+r3 and r2< r1+r3 and r3<r1+r2:
    print('Os segmentos {}, {} e {} formam um triângulo'.format(r1,r2,r3))

else:
    print('Os segmentos {}, {} e {} não formam um triângulo'.format(r1,r2,r3))