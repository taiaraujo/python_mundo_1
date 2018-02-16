# DESAFIO 02
# descobrir se começa com Santo
cid = str(input('Informe o nome da cidade: ')).strip()
print(cid[:5].upper() == 'SANTO')

# DESAFIO 025
# descobrir se tem Silva no nome
nome = str(input('Informe seu nome: ')).strip()
print('silva' in nome.lower())