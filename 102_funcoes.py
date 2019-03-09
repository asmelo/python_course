def fatorial(nr, show=False):
    fat = 1;
    for c in range(nr, 0, -1):
        fat *= c
        if show:
            fim = ' * '
            if c == 1:
                fim = ' '
            print(c, end=fim)
    if show:
        print(f' = {fat}')
    else:
        print(f'O fatorial vale {fat}.')

fatorial(5, True)