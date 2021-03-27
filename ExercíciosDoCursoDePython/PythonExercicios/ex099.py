from time import sleep


def valores(*num):
    print('-=' * 30)
    print('Analisando os valores passados...')
    for i, v in enumerate(num):
        print(f'{v}', end=' ')
        sleep(0.5)
    if num != ():
        print(f'Foram informados {len(num)} valores ao todo.')
        print(f'O maior valor informado foi {max(num)}.')
    else:
        print('Foram informados 0 valores ao todo.')
        print('O maior valor informado foi 0.')


valores(2, 9, 4, 5, 7, 1)
valores(4, 7, 0)
valores(1, 2)
valores(6)
valores()
