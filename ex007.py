# DESAFIO 014
# conversor de temperatura
c = float(input('Informe a temperatura em ºC: '))
print('Temperatura em ºF:{:.1f}'.format((c*1.8)+32))
f = float(input('Informe a temperatura em ºF: '))
print('Temperatura em ºC: {:.1f}'.format((f-32)/1.8))

# DESAFIO 015
# aluguel de carro
km = float(input('Quilometros rodados? '))
d = int(input('Quantidade de dias? '))
p = (60*d)+(0.15*km)
print('Valor a pagar: {:.2f}'.format(p))
