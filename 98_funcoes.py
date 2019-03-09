def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} a {fim} de {passo} em {passo}')
    if fim < inicio:
        fim -= 1
        if passo > 0:
            passo *= -1
    else:
        fim += 1
    for c in range(inicio, fim, passo):
        print(c, end=' ')
    print('FIM')


contador(1, 10, 1)
contador(10, 0, 2)

print('-=' * 30)
print('Agora é sua vez de personalizar a contagem!')
início = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
print('-=' * 30)
contador(início, fim, passo)