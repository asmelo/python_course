exp = input('Digite uma expressão: ')
qtdA = 0
qtdB = 0
for item in exp:
    if item == '(':
        qtdA += 1
    if item == ')':
        qtdB += 1
if qtdA == qtdB:
    print('A expressão está correta')
else:
    print('A expressão está errada')