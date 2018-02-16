# DESAFIO 035
a = float(input('Informe o lado a: '))
b = float(input('Informe o lado b: '))
c = float(input('Informe o lado c: '))
sub = b - c
if sub < 0:
    sub = sub * (-1)
soma = b + c
if sub < a < soma:
    print('forma triângulo')
else:
    print('não forma triangulo')