nr = int(input('Digite um número: '))
resultado = 'É primo'
for c in range(2, nr):
    if nr % c == 0:
        resultado = 'Não é primo'
        break
print(resultado)