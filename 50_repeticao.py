soma = 0;
for c in range(0,6):
    nr = int(input('Digite um número: '))
    if nr % 2 == 0:
        soma += nr
print('A soma é ', soma)