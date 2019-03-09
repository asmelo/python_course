import datetime
ano = int(input('Ano de nascimento: '))
print('ano: ', ano)
anoAtual = int(datetime.datetime.now().year)
print('anoAtual: ', anoAtual)
idade = anoAtual - ano
print('idade: ', idade)
if idade == 18:
    print('Este é seu ano de alistamento')
elif idade < 18:
    print('Faltam {} ano(s) para seu alistamento'.format(18 - idade))
else:
    print('Já se passaram {} anos do seu alistamento'.format(idade - 18))