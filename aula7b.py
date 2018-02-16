nome = input('Qual seu nome? ')
print('Prazer em te conhecer, {:=^20}!'.format(nome))

# :=^ centraliza o print usando '='
# exemplo: =====ANA=====

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('Soma: {}, Produto: {}, Divisão: {:.2f}, Divisão inteira: {}, Potência: {}'.format(s, m, d, di, e))
