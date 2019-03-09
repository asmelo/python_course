alunos = list()
flag = 's'
while flag in 'sS':
    aluno = list()
    aluno.append(input('Nome: '))
    notas = list()
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    aluno.append(notas[:])
    aluno.append((notas[0] + notas[1]) / 2)
    alunos.append(aluno[:])
    aluno.clear()
    notas.clear()
    flag = input('Quer continuar? [S/N]: ')
print('-=' * 30)
print(f'{"no.":<4} {"NOME":<15} {"MÉDIA":<7}')
print('-' * 45)
for idx,aluno in enumerate(alunos):
    print(f'{idx:<4} {aluno[0]:<15} {aluno[2]:<7.1f}')
print('-' * 45)

idx = 0
while True:
    idx = int(input('Mostrar notas de qual aluno? (999 iterrompe): '))
    if idx == 999:
        break
    print(f'Notas de {alunos[idx][0]} são {alunos[idx][1]}')
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>')