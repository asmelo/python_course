lista = []
maior = 0
menor = -1
for c in range(0,5):
    nr = int(input('Digite um valor: '))
    lista.append(nr)
    if nr > maior:
        maior = nr
    if menor is -1 or nr < menor:
        menor = nr
print(f'Você Digitou os valores {lista}')
print(f'O maior valor digitado foi o {maior} e está nas posições ', end='')
for idx, nr in enumerate(lista):
    if nr is maior:
        print(idx, end='...')
print('')
print(f'O menor valor digitado foi o {menor} e está na posição ', end='')
for idx, nr in enumerate(lista):
    if nr is menor:
        print(idx, end='...')