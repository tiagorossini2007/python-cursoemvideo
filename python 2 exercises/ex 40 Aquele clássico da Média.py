n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
ntotal = (n1 + n2) / 2
if ntotal >= 6:
    print("A média é boa! Parabéns!")
elif ntotal < 6 and ntotal > 5:
    print("você está de recuperação! Estude mais um pouco!")
else:
    print("Infelizmente você foi reprovado! Estude mais para a próxima!")