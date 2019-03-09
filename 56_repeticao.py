soma = 0
maisVelho = ''
maior = 0
qtd = 0
for c in range(0,4):
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo (M ou F): ')
    soma += idade
    if (sexo == 'M') & (idade > maior):
        maior = idade
        maisVelho = nome
    if (sexo == 'F') & (idade < 20):
        qtd += 1
print('A média de idade é ', soma/4)
print('O home é mais velho é', maisVelho)
print('Mulheres com menos de 20 anos: ', qtd)