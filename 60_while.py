nr = int(input('Digite um número: '))
fat = 1
while nr >= 1:
    fat *= nr
    nr -= 1
print('O fatoral é {}'.format(fat))