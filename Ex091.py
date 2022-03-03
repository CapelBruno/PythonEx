#Ex. Crie um programa onde sejam sorteados 4 números em um jogo de dados, no fim os coloque em ordem por quem fez mais pontos.

import random
import time
from operator import itemgetter

jogo = {'Jogador1': random.randint(1, 6),
        'Jogador2': random.randint(1, 6),
        'Jogador3': random.randint(1, 6),
        'Jogador4': random.randint(1, 6)}
ranking = []
print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado. ')
    time.sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)     #Ordena e pega os números da posição 1 da conjunto de items(dado).
for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]}. ')
    time.sleep(1)