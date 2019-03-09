from datetime import date

dados = dict()
dados['nome'] = input('Digite o nome: ')
ano = int(input('Digite o ano de nascimento: '))
anoAtual = date.today().year
dados['idade'] = anoAtual - ano
dados['ctps'] = int(input('Digite a carteira de trabalho: '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Digite o ano de contratação: '))
    dados['salario'] = float(input('Digite o salário: '))

for k, v in dados.items():
    print(f'{k}: {v}')

if dados['ctps'] != 0:
    anosTrabalho = anoAtual - dados['contratacao']
    if anosTrabalho >= 35:
        print('Você já poderia estar aposentado')
    else:
        print(f'Faltam {35 - anosTrabalho} anos para se aposentar')