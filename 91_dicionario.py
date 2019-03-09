from random import randint
from time import sleep
from operator import itemgetter
dicio = dict()
for c in range(1,5):
    nome = 'Jogador_' + str(c + 1)
    dicio[nome] = randint(1, 6)

for k, v in dicio.items():
    print(f'O {k} tirou {v}')
    '''sleep(0.5)'''

print('Ranking dos jogadores')

ranking = sorted(dicio.items(), key=itemgetter(1), reverse=True)
print(ranking)

for idx, c in enumerate(ranking):
    print(f'{idx + 1}o lugar: {c[0]} com {c[1]}')
