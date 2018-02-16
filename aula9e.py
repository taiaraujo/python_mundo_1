# DESAFIO 026
# Quantidade de letras A
# o primeiro e o ultimo A
frase = str(input('Digite uma fase: ')).strip()
print('A letra A aparece {} vezes'.format(frase.lower().count('a')))
print('A primeira letra A aparece na posição: {}'.format(frase.lower().find('a')))
print('A ultima letra A aparece na posição: {}'.format(frase.lower().rfind('a')))

# DESAFIO 027
# primeiro e ultimo nome de uma pessoa
nome = str(input('Digite seu nome: ')).strip()
n = nome.split()
print('Seu primeiro nome: {}'.format(n[0]))
print('Seu ultimo nome: {}'.format(n[len(n)-1]))

