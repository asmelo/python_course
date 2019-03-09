extenso = ('um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
valores = (1,2,3,4,5,6,7,8,9,10)
vlr = int(input('Digite um número entre 1 e 10: '))
while vlr not in valores:
    vlr = int(input('Tente novamente. Digite um número 1 e 10: '))
print(f'O valor por extenso é {extenso[vlr-1]}')