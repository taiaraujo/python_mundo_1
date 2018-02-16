# exemplos de condicionais
tempo = int(input('Quantos anos tem seu carro: '))
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')

# outra maneira com média
# condição simplificada
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('Média: {}'.format(m))
print('PARABÉNS' if m >= 5 else 'ESTUDE MAIS')
