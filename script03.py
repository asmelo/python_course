import random
usr = input('Escolha um valor: ').lower()
lista = ['pedra', 'papel', 'tesoura']
if usr not in lista:
    print('Valor inválido')
else:
    pc = random.choice(lista)
    print('pc: ', pc)
    if usr == 'pedra':
        if pc == 'pedra':
            print('Empatou')
        elif pc == 'papel':
            print('Perdeu')
        elif pc == 'tesoura':
            print('Venceu')
    elif usr == 'papel':
        if pc == 'pedra':
            print('Venceu')
        elif pc == 'papel':
            print('Empatou')
        elif pc == 'tesoura':
            print('Perdeu')
    elif usr == 'tesoura':
        if pc == 'pedra':
            print('Perdeu')
        elif pc == 'papel':
            print('Venceu')
        elif pc == 'tesoura':
            print('Empatou')
