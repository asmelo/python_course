pessoas = list()
maior = 0
menor = -1
flag = 's'
while flag in 'sS':
    dados = list()
    dados.append(input('Nome: '))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    if dados[1] > maior:
        maior = dados[1]
    if menor == -1 or dados[1] < menor:
        menor = dados[1]
    dados.clear()
    flag = input('Deseja continuar? [S, N]: ')
print(f'Ao todo você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior} Kg. Peso de ', end='')
for pessoa in pessoas:
    if pessoa[1] == maior:
        print(f'{pessoa[0]}', end=' ')
print('')
print(f'O menor peso foi de {menor} Kg. Peso de ', end='')
for pessoa in pessoas:
    if pessoa[1] == menor:
        print(f'{pessoa[0]}', end=' ')