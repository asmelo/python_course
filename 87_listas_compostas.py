lista = list()
somaPares = soma3Coluna = maior = 0
for l in range(0, 3):
    linha = list()
    lista.append(linha)
    for c in range(0, 3):
        vlr = int(input(f'Digite um valor para [{l}, {c}]: '))
        lista[l].append(vlr)
print('-=' * 30)
for idxLin, l in enumerate(lista):
    for idxCol, c in enumerate(l):
        print(f'[ {c} ]', end=' ')
        if c % 2 == 0:
            somaPares += c
        if idxCol == 2:
            soma3Coluna += c
        if idxLin == 1:
            if c > maior:
                maior = c
    print('')
print(f'A soma dos valores pares é {somaPares}.')
print(f'A soma da coluna 3 é {soma3Coluna}.')
print(f'O maior valor da linha 2 é {maior}.')

