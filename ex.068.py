from random import randint
n = jogadapc = total = c = 0
resp = 'Ss'
poui = palpite = ''
print('=-'*12)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*12)
while True:
    n = int(input('Digite um valor: '))
    palpite = str(input('PAR OU ÍMPAR? [P/I] ')).upper()
    jogadapc = randint(0, 10)
    total = n + jogadapc
    if (total % 2) == 0:
        poui = 'Par'
    else:
        poui = 'Ímpar'
    print('=-'*12)
    print(f'Você jogou {n} e o computador jogou {jogadapc}. Total {total} deu {poui}')
    if poui == 'Par' and palpite in 'Pp':
        if (total % 2) == 0 and palpite in 'Pp':
            print('Você venceu!! :)')
        else:
            print('Você perdeu :(')
    elif poui == 'Ímpar' and palpite in 'Ii':
        if (total % 2) != 0 and palpite in 'Ii':
            print('Você venceu!! :)')
        else:
            print('Você perdeu :(')

    print('-='*12)

    resp = str(input('Gostaria de continuar? [S/N] '))
    c = c + 1
    if resp in 'Nn':
        print('-='*12)
        print('Obrigado por jogar')
        print(f'Você jogou {c} vezes')
        break

