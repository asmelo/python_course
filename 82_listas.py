flag = 's'
lista = list()
pares = list()
ímpares = list()
while flag in 'sS':
    lista.append(int(input('Digite um valor: ')))
    flag = input('Deseja continuar? [S/N]')
print(f'A lista completa é {lista}')
for c in lista:
    if c % 2 == 0:
        pares.append(c)
    else:
        ímpares.append(c)
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {ímpares}')