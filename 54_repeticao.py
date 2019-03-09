from datetime import date
anoAtual = date.today().year
maior = 0
menor = 0
for c in range(0,7):
    ano = int(input('Digite o ano do seu nascimento: '))
    idade = anoAtual - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('Maiores de 21: ', maior)
print('Menores de 21: ', menor)
