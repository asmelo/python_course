import random
nr = random.randrange(0, 10)
usr = 11
qtd = 0
while nr != usr:
    usr = int(input('Digite um número: '))
    qtd += 1
print('Você acertou!')
print('Você precisou de {} tentativas'.format(qtd))