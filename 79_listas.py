lista = list()
flag = 's'
while flag == 's':
    nr = int(input('Digite um valor: '))
    if nr in lista:
        print('Esse valor já existe, não vou adicionar')
    else:
        lista.append(nr)
        print('Valor adicionado à lista')
    flag = input('Deseja continuar? (S, N): ').lower()
print('-=' * 30)
ord = lista.sort(reverse=True)
print(f'Você digitou os valores {lista}')
print(f'Você digitou os valores {ord}')