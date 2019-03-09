tupla = ('casa', 'armario', 'danca', 'pedreiro', 'luta')
for palavra in tupla:
    print(f'Vogais presente na palavra {palavra}: ', end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(f'{letra}', end=' ')
    print('')