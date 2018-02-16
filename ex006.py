# DESAFIO 005
n = int(input('Digite um valor: '))
print('Número: {}\nAntecessor: {}\nSucessor: {}'.format(n, n-1, n+1))

# DESAFIO 006
print('\nDobro: {}\nTriplo: {}\nRaiz quadrada: {}'.format(n*2, n*3, n**(1/2)))

# DESAFIO 007
# Média de duas notas
n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
print('Média do aluno: {}'.format((n1+n2)/2))

# DESAFIO 008
# Transformar metros em centimetros e milimetros
M = float(input('Digite valor em metros: '))
print('Metros: {}, centimetros: {}, milimetros: {}'.format(M, M*100, M*1000))

# DESAFIO 009
# TABUALA "simples"
t = int(input('Informe um valor para a tabuada: '))
print('{}\nx1={}\nx2={}\nx3={}\nx4={}\nx5={}\nx6={}\nx7={}\nx8={}\nx9={}\nx10={}'.format(t, t*1, t*2, t*3, t*4, t*5, t*6, t*7, t*8, t*9, t*10))

# DESAFIO 010
# Conversão de real para dolar
real = float(input('Informe valor em rais: '))
print('Conversão para dolar: {}'.format(real/3.27))

# DESAFIO 011
l = float(input('Informe a lagura da parede: '))
h = float(input('Informe a altura da parede: '))
print('Sua área é de: {} e iremos precisar de {:.1f} litros de tinta'.format(l*h, (l*h)/2))

# DESAFIO 012
# desconto de um valor (5%)
valor = float(input('Informe o preço do produto: '))
print('Produto com desconto: {}'.format(valor-(valor*0.05)))

# DESAFIO 013
# aumento do salario (15%)
sal = float(input('Salario atual: '))
print("Salario com aumento: {}".format(sal+(sal*0.15)))
