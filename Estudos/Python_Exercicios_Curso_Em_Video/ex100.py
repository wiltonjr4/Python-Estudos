from time import sleep
from random import randint
numeros = []


def soteador():
    for v in range(0, 5):
        num = randint(1, 5)
        numeros.append(num)
    print('Sorteando 5 valores da lista: ', end='')
    for i, v in enumerate(numeros):
        print(f'{v}', end=' ')
        sleep(0.5)
    print('PRONTO!')


def somaPar():
    par = 0
    for i, v in enumerate(numeros):
        if v % 2 == 0:
            par += v
    print(f'Somando os valores pares de {numeros}, temos {par}')


soteador()
somaPar()
