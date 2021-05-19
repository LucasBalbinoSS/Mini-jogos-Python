from random import randint as rdt
from time import sleep as sp

itens = ('Pedra', 'Papel', 'Tesoura')
computador = rdt(0, 2)

print('''\033[37;1mJogadas:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

player = int(input('Escolha sua jogada: '))

print('\033[31;1mJO')
sp(1)
print('KEN')
sp(1)
print('PÔ\033[m')

print('\033[31;1m* \033[m' * 10)
print('O computador escolheu \033[1m%s\033[m!' % itens[computador])
print('Você jogou \033[1m%s\033[m!' % itens[player])
print('\033[31;1m* \033[m' * 10)


if computador == 0:  #PEDRA
    if player == 0:
        print('EMPATE!')
    elif player == 1:
        print('VOCÊ GANHOU DO COMPUTADOR!!! PARABÉNS!!!')
    elif player == 2:
        print('VOCÊ PERDEU...')
    else:
        print('\033[31;4mJOGADA INVÁLIDA, TENTE NOVAMENTE\033[m')

elif computador == 1:   #PAPEL
    if player == 0:
        print('VOCÊ PERDEU...')
    elif player == 1:
        print('EMPATE!')
    elif player == 2:
        print('VOCÊ GANHOU DO COMPUTADOR!!! PARABÉNS!!!')
    else:
        print('\033[31;4mJOGADA INVÁLIDA, TENTE NOVAMENTE\033[m')

elif computador == 2:   #TESOURA
    if player == 0:
        print('VOCE GANHOU DO COMPUTADOR!!! PARABÉNS!')
    elif player == 1:
        print('VOCÊ PERDEU...')
    elif player == 2:
        print('EMPATE!')
    else:
        print('\033[31;4mJOGADA INVÁLIDA, TENTE NOVAMENTE\033[m')