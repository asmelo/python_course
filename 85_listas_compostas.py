pares = list()
ímpares = list()
lista = list()
lista.append(pares)
lista.append(ímpares)
for c in range(0,7):
    vlr = int(input('Digite um valor: '))
    if vlr % 2 == 0:
        lista[0].append(vlr)
    else:
        lista[1].append(vlr)
lista[0].sort()
lista[1].sort()
print(f'Pares: {lista[0]}')
print(f'Ímpares: {lista[1]}')