def ficha(nome='<desconhecido>', gol=0):
    print(f'O jogador {nome} fez {gol} gol(s) no campeonato')

nome = input('Nome do jogador: ')
gol = input('Número de gols: ')
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if nome.strip() == '':
    ficha(gol=gol)
else:
    ficha(nome, gol)