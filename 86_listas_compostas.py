lista = list()
for l in range(0, 3):
    linha = list()
    lista.append(linha)
    for c in range(0, 3):
        lista[l].append(int(input(f'Digite um valor para [{l}, {c}]: ')))
print('-=' * 30)
for l in lista:
    for c in l:
        print(f'[ {c} ]', end=' ')
    print('')