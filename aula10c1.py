# DESAFIO 032
# BISSEXTO
from datetime import date
ano = int(input('Informe o ano ou Insira (0) para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year # 'retira' o ano da maquina
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Ano bissexto')
else:
    print('não bissexto')