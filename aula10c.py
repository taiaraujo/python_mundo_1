# DESAFIO 029
# calculando multa
v = float(input('Informe a sua velocidade: '))
if v > 80.0:
    print('Você foi multado! \n Valor da multa: {:.2f}'.format((v-80)*7))

# DESAFIO 030
# PAR OU IMPAR
num = int(input('Digite um valor inteiro: '))
print('PAR' if num % 2 == 0 else 'IMPAR')

# DESAFIO 031
# VALOR DA VIAGEM
via = float(input('Informa a distância da sua viagem: '))
if via > 200:
    preco = via * 0.45
else:
    preco = via * 0.5
print('Valor da viagem: {:.2f} reais'.format(preco))

# DESAFIO 032
# ANO BISSEXTO
ano = int(input('Informe o ano: '))
print('BISSEXTO' if ano % 4 == 0 else 'NÃO - BISSEXTO')
