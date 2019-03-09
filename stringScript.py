ano = int(input('Digite um ano'))
resto = ano%4
print('Resto: ', resto)
if resto != 0:
    print('É um ano bissexto')
else:
    resto = ano % 100
    if resto != 0:
        print('É um ano bissexto')
    else:
        resto = ano % 400
        if resto != 0:
            print('Não é um ano bissexto')
        else:
            print('É um ano bissexto')