p1 = int(input("Digite o primeiro lado do triângulo: "))
p2 = int(input("Digite o segundo lado do triângulo: "))
p3 = int(input("Digite o terceiro lado do triângulo: "))
if p1 == p2 or p1 == p3 or p2 == p3:
    print("O triângulo é isósceles.")
elif p1 == p2 == p3:
    print("O triângulo é equilátero.")
elif p1 != p2 and p1 != p3 and p2 != p3:
    print("O triângulo é escaleno.")
else:
    print("Os valores digitados não formam um triângulo.")