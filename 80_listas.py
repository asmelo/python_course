lista = list()
for c in range(0,5):
    nr = int(input('Digite um número: '))
    if len(lista) == 0:
        lista.append(nr)
    else:
        for idx, val in enumerate(lista):
            if val > nr:
                lista.insert(idx, nr)
                break
            if idx == len(lista) - 1:
                lista.append(val)
print(f'A lista ordenada é {lista}')