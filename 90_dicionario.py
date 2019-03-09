dicio = dict()
dicio['nome'] = input('Qual o nome do aluno? ')
dicio['nota'] = float(input('Qual a nota do aluno? '))
dicio['situacao'] = 'Aprovado' if dicio['nota'] >= 7.0 else 'Reprovado'

for k,v in dicio.items():
    print(f'O {k} é {v}')