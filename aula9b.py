# DESAFIO 022
# receba um nome
nome = str(input('Informe um nome: ')).strip()
# todas as letras maiusculas
print(nome.upper())
# todas as letras minusculas
print(nome.lower())
# quantas letras ao todo sem espaços
print('Quantidade de letas {}'.format(len(nome) - nome.count(' ')))
#quantas letras tem o primeiro nome
separa = nome.split()
print('Primeiro nome: {} => tem {} letras'.format(separa[0], len(separa[0])))
