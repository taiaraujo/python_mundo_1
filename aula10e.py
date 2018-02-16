# DESAFIO 034
# aumento de salario
sal = float(input('Informe o salario: '))
if sal > 1250:
    nsal = sal + (sal * 0.10)
else:
    nsal = sal + (sal * 0.15)

print('salario era: {}\n Novo salario: {}'.format(sal, nsal))
