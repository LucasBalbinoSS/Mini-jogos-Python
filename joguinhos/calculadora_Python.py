from time import sleep as slp

print('      \033[1m-_-_-_-_-_-_-\033[m')
print('       \033[1;4mCALCULADORA\033[m')
print('      \033[1m-_-_-_-_-_-_-\033[m')

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

print()

escolha = int(input('''O que você deseja fazer com esses valores?
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa
    Escolha: '''))

while escolha != 5:
    if escolha < 1:
        print('\033[1;4;31m-_' * 18)
        print('ERRO\nEscolha uma opção de 1 a 5!')
        print('-_' * 18)

    elif escolha > 5:
        print('\033[1;4;31m-_' * 18)
        print('ERRO\nEscolha uma opção de 1 a 5!')
        print('-_' * 18)

    elif escolha == 1:
        print('-_' * 18)
        print('A soma entre %i e %i é igual a %i' % (n1, n2, n1 + n2))
        print('-_' * 18)
        slp(4)

    elif escolha == 2:
        print('-_' * 18)
        print('A multiplicação entre %i e %i é igual a %i' % (n1, n2, n1 * n2))
        print('-_' * 18)
        slp(4)

    elif escolha == 3:
        if n1 > n2:
            print('-_' * 18)
            print('O maior número entre %i e %i é o \033[1m%i\033[m' % (n1, n2, n1))
            print('-_' * 18)
        elif n2 > n1:
            print('-_' * 18)
            print('O maior número entre %i e %i é o \033[1m%i\033[m' % (n1, n2, n2))
            print('-_' * 18)
        else:
            print('-_' * 18)
            print('Os números %i e %i são iguais' % (n1, n2))
            print('-_' * 18)
        slp(4)

    elif escolha == 4:
        print('-_' * 18)
        print('Opa, vamos lá novamente!')
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
        print('-_' * 18)
        print('O que você deseja fazer com esses novos valores?')

    escolha = int(input('''\033[m
     [ 1 ] Somar
     [ 2 ] Multiplicar
     [ 3 ] Maior
     [ 4 ] Novos números
     [ 5 ] Sair do programa
     Escolha: '''))

print('Saindo...')
slp(2)
print('-_' * 18)
print('Tenha uma boa noite!...zzz...')
