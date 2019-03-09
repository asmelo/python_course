'''
Python usa Código ANSI
    Style
        0: none
        1: bold
        4: underline
        7: negativa

    Text color
        30: branco
        31: vermelho
        32: verde
        33: amarelo
        34: azul
        35: roxo
        36: magento
        37: cinza

    Background color
        40: branco
        41: vermelho
        42: verde
        43: amarelo
        44: azul
        45: roxo
        46: magento
        47: cinza
'''

print('\033[4;33;44mOlá Mundo\033[m')
#\033[0;33;41m
#\033[4;33;44m
##\033[1;35;43m
#\033[30;42m
#\033[m #cores padrão
#\033[7;30m
nome = 'Alexandre'
print('Olá! Muito prazer em te conhecer {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))
cores = {'limpa':'\033[m', 'amarelo':'\033[4;33m'}
print('Olá! Muito prazer em te conhecer {}{}{}!!!'.format(cores['amarelo'], nome, cores['limpa']))