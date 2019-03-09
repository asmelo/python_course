from random import randint
from time import sleep

def sorteia(numeros):
    print('Sorteando 5 valores da lista: ', end=' ')
    for c in range(0,5):
        val = randint(1, 10)
        numeros.append(val)
        print(f'{val}', end=' ')
        sleep(0.5)
    print('PRONTO')

def somaPar(numeros):
    s = 0
    for c in numeros:
        if c % 2 == 0:
            s += c
    print(f'Somando os valores pares de {numeros}, temos {s}')

numeros = list()
sorteia(numeros)
somaPar(numeros)