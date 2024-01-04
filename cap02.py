# IPython é um shell de Python completo a bastante útil para análise de dados
# pip install ipython
# para usar no terminal do vscode bata digitar ipython na linha de comando dentro do venv

# FUNÇÕES
# Em Python definimos as funções usando o def:
def double(x): 
   """
      Nesse ponto, você coloca um docstring opcional para descrever a função.
      Por exemplo, esta função multiplica a entrada por 2.
   """
   return x * 2

def apply_to_one(f):
   """Chama a função f usando 1 como argumento"""
   return f(1)

my_double = double            #refere-se à função x já definida
x = apply_to_one(my_double)   #igual a 2

#funções lambdas são pequenas funções anônimas
y = apply_to_one(lambda x: x + 4)

another_double = lambda x: 2 * x #não faça isso

def another_double(x):
   """Faça isso"""
   return 2 * x

#Os parâmetros da função também podem receber argumentos padrão:
def my_print(message = "my default message"):
   print(message)

my_print("hello") #imprime 'hello'
my_print()        #imprime 'my default message'

#STRINGS

#A barra invertida '\' serve para codificar caracteres esoeciais. Como o caractere tab: \t
tab_string = "\t"    # representa o caractere tab
len(tab_string)      # é 1

#para usar o carctere de barra invertida como em nosmes de diretórios
# podemos criar strings brutas com r""
not_tab_string = r"\t"     # representa os caracteres '\' e 't'
len(not_tab_string)        # é 2

#f-string
first_name = "Gabriel"
last_name = "Ribeiro"

full_name = f"{first_name} {last_name}"
print(full_name)

#EXCEÇÕES
try:
   print(0 / 0)
except ZeroDivisionError:
   print("cannot divide by zero")

#LISTAS
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

last = x[-1]            #igual a 9, 'Pythonic' para o último elemento
penultimate = x[-2]     #igual a 8, 'Pythonic' para o penúltimo elemento
x[0] = -1               #agora x é [-1, 1, 2, ..., 8, 9]

#É possível utilizar colchetes para fatiar as listas. A fatia i:j contém 
#os elementos de i (incluído) a j (não incluído). Se o início da fatia não for
#explicitado, ele começará no início da lista; se o final não for indicado,
#ela terminará no final da lista

first_three = x[:3]
three_to_end = x[3:]
one_to_four = x[1:5]
last_three = x[-3:]

#uma fatia pode receber um terceiro argumento, stride (passo)
every_third = x[::3]             #[-1, 3, 6, 9]
five_to_three = x[5:2:-1]        #[5, 4, 3]

#Para concatenar as listas é possível usar o .extend(['lista']) ou a adição x = [1, 2, 3] y = x + [4, 5, 6]; x é inalterado
#outro modo é o método .append(0)
x = [1, 2, 3]
x.append(0)          #x agora é [1, 2, 3, 0]

#Muitas vezes é conveniente descompactar as listas quando sabemos quantos elementos elas contém
x, y = [1, 2]        #agora x é 1, y é 2
#usa-se sublinhado _ para indicar o valor que será descartado:
_, y = [1, 2]        #agora y == 2, não considerou o primeiro elemento

#TUPLAS
#são como listas mas não podem ser modificadas
#são uma forma eficaz de usar funções para retornar múltiplos valores:
def sum_and_product(x, y):
   return (x + y), (x * y)

sp = sum_and_product(2,3)        #sp é (5, 6)
s, p = sum_and_product(5, 10)    #s é 15, p é 50

#As tuplas (e as listas) podem ser usadas em atribuições múltiplas:
x, y = 1, 2       #agora x é 1 e y é 2
x, y = y, x       #forma 'Pythonic' de trocar variáveis; agora x é 2 e y é 1

#DICIONÁRIOS
# Associa valores a chaves
grades = {"Joel": 80, "Tim":95}
#para pesquisar o valor de uma chave, pode-se usar colchetes:
joels_grade = grades["Joel"]        #igual a 80

#aparecerá KeyError se procurar por uma chave que não está no dicionário
try:
   kates_grade = grades["Kate"]
except KeyError:
   print("no grade for Kate!")

#Para verificar a existência de uma chave é possível usar o in:
joel_has_grade = "Joel" in grades         #Verdadeiro
kate_has_grade = "Kate" in grades         #Falso
#o mpetodo .get() retorna um valor padrão ao invés de uma exceção:
joels_grade = grades.get("Joel", 0)    #igual a 80
kates_grade = grades.get("Kate", 0)    #igual a 0
no_ones_grade = grades.get("No One")   #o padrão é None
#é possível atribuir valores usando colchetes:
grades["Tim"] = 99         #substitui o valor anterior
grades["Kate"] = 100       #adiciona uma terceira entrada

#DEFAULTDICTC
#Para usar os defaultdicts devemos importá-los das collections:
from collections import defaultdict
document = ["Lista", "supostamente", "aleatória"]
word_counts = defaultdict(int)      #int() produz 0
for word in document: #document é uma lista de palavras
   word_counts[word] += 1

#CONTADORES
# O Counter (contador) converte uma sequencia de valores em algo precido com um defaultdict(int) mapeando as chaves correspondentes às contagens
from collections import Counter
c = Counter([0, 1, 2, 0])  #c é basicamente {0: 2, 1: 1, 2: 1}

#Uma instância Counter contém um método most_common bastante útil:

#imprima as 10 palavras mais comuns e suas contagens
for word, count in word_counts.most_common(10):
   print(word, count)

#CONJUNTO (set) - coleção de elementos *distintos*
primes_bellow_10 = {2, 3, 5, 7} #Não funciona com conjuntos bvazios pos {} é um dict vazio e não um set. Nesse cso deve-se usar o set()
s = set()
s.add(1)       #s agora é {1}
s.add(2)       #s é {1, 2}
s.add(2)       #s ainda é {1, 2}

#FLUXO DE CONTROLE 
parity = "even" if x % 2 == 0 else "odd"     #operador ternário

for x in range(10):
   if x == 3:
      continue #vá imediatamente para a próxima iteração
   if x == 5:
      break
   print(x)

#VERACIDADE
# Todos os exemplos a seguir são falsos:
#    False
#    None
#    [] uma list vazia
#    {} um dict vazio
#    ""
#    set()
#    0
#    0.0
   
#CLASSIFICAÇÃO
# Em Python, toda lista tem um método sort()
x = [4, 1, 3, 2]
y = sorted(x)     # y agora é [1, 2, 3, 4], x não mudou
x.sort()          # agora x é [1, 2, 3, 4]