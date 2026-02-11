fatiar uma string em pedaços: 
ex [2:] (começa no 2 e vai ate o final
qualquer espaço conta


📊 TIPOS DE DADOS (Data Types)
Básicos:
int - Números inteiros
pythonidade = 25
numero = -10
grande = 1000000
float - Números decimais
pythonaltura = 1.75
preco = 19.90
pi = 3.14159
str - Strings (texto)
pythonnome = "Tiago"
frase = 'Python é legal'
multiline = """Texto
em várias
linhas"""
bool - Booleanos (True/False)
pythonativo = True
maior_idade = False
None - Valor nulo
pythonresultado = None

Coleções:
list - Listas (mutáveis, ordenadas)
pythonnumeros = [1, 2, 3, 4, 5]
nomes = ["Ana", "João", "Maria"]
mista = [1, "texto", 3.14, True]
tuple - Tuplas (imutáveis, ordenadas)
pythoncoordenadas = (10, 20)
rgb = (255, 0, 128)
dados = ("Tiago", 17, True)
dict - Dicionários (chave-valor)
pythonpessoa = {
    "nome": "Tiago",
    "idade": 17,
    "cidade": "São Paulo"
}
set - Conjuntos (únicos, não ordenados)
pythonnumeros = {1, 2, 3, 4, 5}
frutas = {"maçã", "banana", "laranja"}

🔤 FUNÇÕES DE STRING
Formatação:
upper() - Maiúsculas
pythonnome = "tiago"
print(nome.upper())  # TIAGO
lower() - Minúsculas
pythonnome = "TIAGO"
print(nome.lower())  # tiago
capitalize() - Primeira letra maiúscula
pythonfrase = "python é legal"
print(frase.capitalize())  # Python é legal
title() - Primeira letra de cada palavra
pythonfrase = "curso em vídeo"
print(frase.title())  # Curso Em Vídeo
strip() - Remove espaços
pythontexto = "  python  "
print(texto.strip())  # "python"
print(texto.lstrip())  # "python  " (esquerda)
print(texto.rstrip())  # "  python" (direita)

Verificação:
startswith() - Começa com
pythonnome = "Tiago"
print(nome.startswith("Ti"))  # True
endswith() - Termina com
pythonarquivo = "foto.jpg"
print(arquivo.endswith(".jpg"))  # True
isdigit() - É número?
pythontexto = "123"
print(texto.isdigit())  # True
isalpha() - É letra?
pythontexto = "Python"
print(texto.isalpha())  # True
isalnum() - É letra ou número?
pythontexto = "Python3"
print(texto.isalnum())  # True
isspace() - É espaço?
pythontexto = "   "
print(texto.isspace())  # True

Busca e Substituição:
find() - Encontrar posição
pythonfrase = "Python é legal"
print(frase.find("é"))  # 7
print(frase.find("Java"))  # -1 (não encontrou)
index() - Igual find, mas dá erro se não achar
pythonfrase = "Python é legal"
print(frase.index("é"))  # 7
count() - Contar ocorrências
pythonfrase = "banana"
print(frase.count("a"))  # 3
replace() - Substituir
pythonfrase = "Python é legal"
print(frase.replace("legal", "incrível"))  # Python é incrível
split() - Dividir string em lista
pythonfrase = "Python é legal"
palavras = frase.split()  # ["Python", "é", "legal"]

csv = "nome,idade,cidade"
dados = csv.split(",")  # ["nome", "idade", "cidade"]
join() - Juntar lista em string
pythonpalavras = ["Python", "é", "legal"]
frase = " ".join(palavras)  # "Python é legal"

Formatação de Strings:
f-strings (moderno, recomendado)
pythonnome = "Tiago"
idade = 17
print(f"Olá, meu nome é {nome} e tenho {idade} anos")
print(f"2 + 2 = {2 + 2}")  # Pode fazer contas
print(f"Preço: R$ {19.9:.2f}")  # 19.90 (2 casas decimais)
.format() (antigo)
pythonnome = "Tiago"
idade = 17
print("Olá, {} tem {} anos".format(nome, idade))
print("Nome: {0}, Idade: {1}".format(nome, idade))
% (muito antigo, evite)
pythonnome = "Tiago"
idade = 17
print("Olá, %s tem %d anos" % (nome, idade))

🔢 FUNÇÕES DE NÚMEROS
abs() - Valor absoluto
pythonprint(abs(-10))  # 10
round() - Arredondar
pythonprint(round(3.7))  # 4
print(round(3.14159, 2))  # 3.14 (2 casas)
pow() - Potência
pythonprint(pow(2, 3))  # 8 (2³)
print(2 ** 3)  # 8 (mesmo resultado)
max() - Maior valor
pythonprint(max(1, 5, 3, 9, 2))  # 9
print(max([1, 5, 3, 9, 2]))  # 9
min() - Menor valor
pythonprint(min(1, 5, 3, 9, 2))  # 1
sum() - Soma
pythonnumeros = [1, 2, 3, 4, 5]
print(sum(numeros))  # 15

Módulo Math:
pythonimport math

math.sqrt(16)      # 4.0 (raiz quadrada)
math.ceil(3.2)     # 4 (arredonda pra cima)
math.floor(3.9)    # 3 (arredonda pra baixo)
math.factorial(5)  # 120 (5!)
math.pi            # 3.14159...
math.e             # 2.71828...
math.sin(math.pi)  # Seno
math.cos(0)        # Cosseno
math.tan(math.pi/4) # Tangente

📋 FUNÇÕES DE LISTAS
append() - Adicionar no final
pythonfrutas = ["maçã", "banana"]
frutas.append("laranja")
print(frutas)  # ["maçã", "banana", "laranja"]
insert() - Adicionar em posição específica
pythonfrutas = ["maçã", "banana"]
frutas.insert(1, "uva")
print(frutas)  # ["maçã", "uva", "banana"]
extend() - Adicionar múltiplos itens
pythonfrutas = ["maçã"]
frutas.extend(["banana", "laranja"])
print(frutas)  # ["maçã", "banana", "laranja"]
remove() - Remover por valor
pythonfrutas = ["maçã", "banana", "laranja"]
frutas.remove("banana")
print(frutas)  # ["maçã", "laranja"]
pop() - Remover por índice e retornar
pythonfrutas = ["maçã", "banana", "laranja"]
ultima = frutas.pop()  # Remove e retorna "laranja"
segunda = frutas.pop(1)  # Remove e retorna "banana"
clear() - Limpar lista
pythonfrutas = ["maçã", "banana"]
frutas.clear()
print(frutas)  # []
index() - Encontrar índice
pythonfrutas = ["maçã", "banana", "laranja"]
print(frutas.index("banana"))  # 1
count() - Contar ocorrências
pythonnumeros = [1, 2, 3, 2, 4, 2]
print(numeros.count(2))  # 3
sort() - Ordenar (modifica a lista)
pythonnumeros = [3, 1, 4, 2]
numeros.sort()
print(numeros)  # [1, 2, 3, 4]

numeros.sort(reverse=True)  # Decrescente
print(numeros)  # [4, 3, 2, 1]
sorted() - Ordenar (cria nova lista)
pythonnumeros = [3, 1, 4, 2]
ordenados = sorted(numeros)
print(ordenados)  # [1, 2, 3, 4]
print(numeros)  # [3, 1, 4, 2] (original não mudou)
reverse() - Inverter
pythonnumeros = [1, 2, 3, 4]
numeros.reverse()
print(numeros)  # [4, 3, 2, 1]
copy() - Copiar lista
pythonoriginal = [1, 2, 3]
copia = original.copy()

📖 FUNÇÕES DE DICIONÁRIOS
keys() - Pegar chaves
pythonpessoa = {"nome": "Tiago", "idade": 17}
print(pessoa.keys())  # dict_keys(['nome', 'idade'])
values() - Pegar valores
pythonprint(pessoa.values())  # dict_values(['Tiago', 17])
items() - Pegar pares chave-valor
pythonprint(pessoa.items())  # dict_items([('nome', 'Tiago'), ('idade', 17)])
get() - Pegar valor (seguro)
pythonprint(pessoa.get("nome"))  # "Tiago"
print(pessoa.get("email", "Não tem"))  # "Não tem" (valor padrão)
update() - Atualizar/adicionar
pythonpessoa.update({"cidade": "SP", "idade": 18})
pop() - Remover e retornar
pythonidade = pessoa.pop("idade")
clear() - Limpar
pythonpessoa.clear()

🔄 FUNÇÕES DE CONVERSÃO
int() - Converter para inteiro
pythonprint(int("10"))  # 10
print(int(3.9))  # 3 (corta decimal)
print(int("1010", 2))  # 10 (binário para decimal)
float() - Converter para float
pythonprint(float("3.14"))  # 3.14
print(float(5))  # 5.0
str() - Converter para string
pythonprint(str(123))  # "123"
print(str(3.14))  # "3.14"
bool() - Converter para booleano
pythonprint(bool(1))  # True
print(bool(0))  # False
print(bool(""))  # False (string vazia)
print(bool("texto"))  # True
list() - Converter para lista
pythonprint(list("Python"))  # ['P', 'y', 't', 'h', 'o', 'n']
print(list((1, 2, 3)))  # [1, 2, 3] (tupla para lista)
tuple() - Converter para tupla
pythonprint(tuple([1, 2, 3]))  # (1, 2, 3)
set() - Converter para conjunto
pythonprint(set([1, 2, 2, 3, 3]))  # {1, 2, 3} (remove duplicados)

🎯 FUNÇÕES BUILT-IN ESSENCIAIS
print() - Imprimir
pythonprint("Olá")
print("Nome:", nome)
print(f"Idade: {idade}")
print("Linha 1", "Linha 2", sep="\n")
print("Sem quebra", end="")
input() - Ler entrada do usuário
pythonnome = input("Qual seu nome? ")
idade = int(input("Qual sua idade? "))
len() - Tamanho/comprimento
pythonprint(len("Python"))  # 6
print(len([1, 2, 3]))  # 3
print(len({"a": 1, "b": 2}))  # 2
type() - Ver tipo
pythonprint(type(10))  # <class 'int'>
print(type("texto"))  # <class 'str'>
print(type([1, 2]))  # <class 'list'>
range() - Criar sequência
pythonprint(list(range(5)))  # [0, 1, 2, 3, 4]
print(list(range(1, 6)))  # [1, 2, 3, 4, 5]
print(list(range(0, 10, 2)))  # [0, 2, 4, 6, 8]
enumerate() - Índice + valor
pythonfrutas = ["maçã", "banana", "laranja"]
for i, fruta in enumerate(frutas):
    print(f"{i}: {fruta}")
# 0: maçã
# 1: banana
# 2: laranja
zip() - Combinar listas
pythonnomes = ["Ana", "João", "Maria"]
idades = [25, 30, 28]
for nome, idade in zip(nomes, idades):
    print(f"{nome} tem {idade} anos")
map() - Aplicar função
pythonnumeros = [1, 2, 3, 4]
dobrados = list(map(lambda x: x * 2, numeros))
print(dobrados)  # [2, 4, 6, 8]
filter() - Filtrar
pythonnumeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4, 6]
any() - Algum é True?
pythonprint(any([False, True, False]))  # True
all() - Todos são True?
pythonprint(all([True, True, True]))  # True
print(all([True, False, True]))  # False

📁 FUNÇÕES DE ARQUIVOS
open() - Abrir arquivo
python# Ler
arquivo = open("dados.txt", "r")
conteudo = arquivo.read()
arquivo.close()

# Escrever
arquivo = open("dados.txt", "w")
arquivo.write("Olá mundo")
arquivo.close()

# Adicionar
arquivo = open("dados.txt", "a")
arquivo.write("\nNova linha")
arquivo.close()

# Forma segura (recomendado)
with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()
    # Fecha automaticamente
Modos de abertura:

"r" - Leitura
"w" - Escrita (sobrescreve)
"a" - Adicionar (append)
"r+" - Leitura e escrita
"rb" - Binário (para imagens, etc.)

Métodos de leitura:
pythonarquivo.read()  # Ler tudo
arquivo.readline()  # Ler uma linha
arquivo.readlines()  # Ler todas as linhas em lista

🎲 MÓDULO RANDOM
pythonimport random

random.random()  # Float entre 0 e 1
random.randint(1, 10)  # Inteiro entre 1 e 10
random.choice([1, 2, 3, 4])  # Escolher aleatório
random.shuffle(lista)  # Embaralhar lista
random.sample([1, 2, 3, 4], 2)  # Pegar 2 aleatórios

⏰ MÓDULO DATETIME
pythonfrom datetime import datetime, date, time

# Data e hora atual
agora = datetime.now()
print(agora)

# Data específica
data = date(2025, 2, 10)
print(data)

# Hora específica
hora = time(14, 30, 0)
print(hora)

# Formatação
agora.strftime("%d/%m/%Y")  # 10/02/2025
agora.strftime("%H:%M:%S")  # 14:30:00