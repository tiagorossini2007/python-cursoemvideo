import math
a = float(input('Qual a medida do ângulo?'))
c = math.cos(math.radians(a))
s = math.sin(math.radians(a))
t = math.tan(math.radians(a))
print('O seno é {}, o cosseno é {}, e o tangente é {}'.format(s, c, t))


