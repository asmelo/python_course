produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15, 'Estojo', 25, 'Tasnferidor', 4.20)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for c in range(0, len(produtos), 2):
    print(f'{produtos[c]:.<30}', end='')
    print(f'R$ {produtos[c+1]:>7.2f}')
print('-' * 40)