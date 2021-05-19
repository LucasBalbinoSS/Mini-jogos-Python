print('\033[1;35m-\033[m' * 20)
print('\033[1;34mJOGO DA ADIVINHAÇÃO')
print('\033[1;35m-\033[m' * 20)

from random import randint

na = randint(0, 5)
n = int(input('Tente adivinhar o número que o computador está pensando: '))
print()

c = 0
while n != na:
    n = int(input('Errou! o número não é %i\nTente acertar novamente: ' % n))
    c += 1
    print()

print()
print('UAU, parabéns!, você acertou! eu estava pensando no número %i!' % na, end='\n')
print('Foram precisas %i tentativas para acertar' % c)
