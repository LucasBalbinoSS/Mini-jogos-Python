from time import sleep as slp
import emoji as emj

an = int(input('Você realizará o réveillon de qual ano?: '))

slp(0.5)
print()
print('A contagem regressiva já irá começar!')
print()
slp(2)

for ano in range(10, 0, -1):
    slp(1)
    print(ano)
slp(1)
print()

print(emj.emojize('\033[1m:sparkles:' * 15, use_aliases=True))
print()

print(' ' * 5, '\033[1;4m%i\033[m' % an)
print('\033[1;31mH\033[1;32mA\033[1;33mP\033[1;34mP\033[1;35mY\033[1;36m', end='')
print(' N\033[1;37mE\033[1;31mW\033[1;32m ', end='')
print('Y\033[1;33mE\033[1;34mA\033[1;35mR\033[1;36m!\033[1;37m!\033[1;31m!\033[m')
print(' ' * 5, '\033[1;4m%i\033[m' % an)

print()
print(emj.emojize('\033[1m:sparkles:' * 15, use_aliases=True))
