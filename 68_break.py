import random
lista = ['par', 'impar']
print('Vamos brincar de par ou impar')
qtd = 0
while True:
    usr = input('O que você é? ')
    pc = random.randrange(0,10)
    usrNum = int(input('Escolha um número de 0 a 10: '))
    soma = usrNum + pc
    if soma % 2 == 0:
        if usr == 'par':
            print('Você venceu!')
            qtd += 1
        else:
            print('Você perdeu!')
            break
    else:
        if usr == 'impar':
            print('Você venceu!')
            qtd += 1
        else:
            print('Você perdeu')
            break
print(f'Você venceu {qtd} vez(es) consecutivas')