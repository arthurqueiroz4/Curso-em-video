from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': 0, 'jogador2': 0, 'jogador3': 0, 'jogador4': 0}
raking = []

print('Valores sorteados:')
for k in jogo.keys():
    jogo[k] = randint(1,  6)
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
raking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(raking):
    print(f'{i + 1}° lugar: {v} com {v[1]}')
    sleep(1)