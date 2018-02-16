# DESAFIO 033
# MAIOR E MENOR DE 3 NUMEROS
n1 = int(input('Informe 1º número: '))
n2 = int(input('Informe 2º número: '))
n3 = int(input('Informe 3º número: '))

if n3 < n1 > n2:
    if n2 > n3:
        print('MAIOR: {}\nMENOR: {}'.format(n1, n3))
    else:
        print('MAIOR: {}\nMENOR: {}'.format(n1, n2))

if n3 < n2 > n1:
    if n1 > n3:
        print('MAIOR: {}\nMENOR: {}'.format(n2, n3))
    else:
        print('MAIOR: {}\nMENOR: {}'.format(n2, n1))

if n1 < n3 > n2:
    if n1 > n2:
        print('MAIOR: {}\nMENOR: {}'.format(n3, n2))
    else:
        print('MAIOR: {}\nMENOR: {}'.format(n3, n1))

