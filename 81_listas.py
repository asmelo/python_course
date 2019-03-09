lista = list()
flag = 's'
while flag == 's':
    lista.append(int(input('Digite um valor: ')))
    flag = input('Deseja continuar (S, N): ')

print(f'Foram digitados {len(lista)} números')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente é {lista}')
if 5 in lista:
    print('O valor 5 está na lista')
else:
    print('O valoro 5 não está na lista')