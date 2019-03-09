def maior(* num):
    print('-=' * 30)
    print('Analisando os valores passados...')
    print(f'{num} Foram informador {len(num)} valores ao todo')
    maior = 0
    for n in num:
        if n > maior:
            maior = n
    print(f'O maior valor é {maior}')

maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()