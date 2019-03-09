from random import randint
from time import sleep

print('-' * 40)
print(f'{"JOGO DA MEGASENA":^40}')
print('-' * 40)
nr = int(input('Digite o número de jogos: '))
jogos = list()
for c in range(0, nr):
    jogo = list()
    for a in range(0, 6):
        vlr = randint(1, 60)
        while vlr in jogo:
            vlr = randint(1, 60)
        jogo.append(vlr)
    jogos.append(jogo[:])
    jogo.clear()
for idx, c in enumerate(jogos):
    print(f'Jogo número {idx}: {c}.')
    sleep(1)