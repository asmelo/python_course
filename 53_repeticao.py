frase = input('Digite uma frase: ')
frase = frase.replace(' ', '')
inverso = ''
for c in range(len(frase) - 1, -1, -1):
    inverso += frase[c]
print('inverso: ', inverso)
if frase == inverso:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')