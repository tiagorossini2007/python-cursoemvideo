f = str(input('Digite uma frase:')).upper()
print('A letra a aparece {} vezes'.format(f.count('A')))
print('Ela aparece pela primeira vez na {} posição'.format(f.find('A')+1))
print('Ela aparece pela ultima vez na {} posição'.format(f.rfind('A')+1))
