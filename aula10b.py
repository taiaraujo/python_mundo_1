# DESAFIO 028
# JOGO DA ADIVINHAÇÃO
import random
import time
pc = random.randrange(0, 5)
print('=#='*20)
num = int(input('Qual o número que o pc escolheu (de 0 a 5): '))
print('=#='*20)
print('PROCESSANDO...')
time.sleep(3)
print('PARABENS' if num == pc else 'O PC VENCEU')
print('usuario: {} \npc: {}'.format(num, pc))
