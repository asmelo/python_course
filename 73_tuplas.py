times = ('São Paulo', 'Flamengo', 'Chapecoense', 'Sport', 'Vasco', 'Sergipe', 'Corinthias', 'Internacional', 'Palmeiras', 'Fluminense')
print('Os primeiros 5 colocados são:')
for time in times[:5]:
    print(time)
print('Os 4 últimos colocados são:')
for time in times[len(times)-4:]:
    print(time)
print('Em ordem:')
print(sorted(times))
posChapeco = times.index('Chapecoense') + 1
print(f'O Chapecoence está na posição {posChapeco}')