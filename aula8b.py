import random
# DESAFIO 020
# SORTEANDO UMA ORDEM NA LISTA
a = input('Insira o primeiro nome: ')
b = input('Insira o segundo nome: ')
c = input('Insira o terceiro nome: ')
d = input('Insira o quarto nome: ')
lista = [a, b, c, d]
random.shuffle(lista)
# shuffle é um sorteio (embaralhamento)
print(lista)