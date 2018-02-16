import math
import random

# DESAFIO 016
# porção inteira

num = float(input('Informe um valor float: '))
print('Porção inteira do valor: {}'.format(math.trunc(num)))

# DESAFIO 017
# hipotenusa do triângulo
co = float(input('Informe o valor do cateto oposto: '))
ca = float(input('Informe o valor do cateto adjacente: '))
h = math.hypot(co, ca)
print('A hipotenusa {:.2f}'.format(h))

# DESAFIO 018
# COS, SEN, TG
ang = float(input('Informe um ângulo: '))
print('cos{:.1f}: {:.2f}'.format(ang, math.cos(math.radians(ang))))
print('sen{:.1f}: {:.2f}'.format(ang, math.sin(math.radians(ang))))
print('tg{:.1f}: {:.2f}'.format(ang, math.tan(math.radians(ang))))

# DESAFIO 019
# sorteio de 4 alunos para apagar o quadro
a = input('Insira o nome do aluno(a): ')
b = input('Insira o nome do aluno(a): ')
c = input('Insira o nome do aluno(a): ')
d = input('Insira o nome do aluno(a): ')
lista = [a, b, c, d]
escolhido = random.choice(lista)
print('Aluno escolhido: {}'.format(escolhido))
