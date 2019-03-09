def voto(ano):
    from datetime import date
    anoAtual = date.today().year
    idade = anoAtual - ano
    if idade < 16:
        return f'Com {idade} anos: Não vota'
    elif idade < 18 or idade >= 60:
        return f'Com {idade} anos: Voto opcional'
    else:
        return f'Com {idade} anos: Voto obrigatório'

ano = int(input('Em que ano você nasceu? '))
print(voto(ano))