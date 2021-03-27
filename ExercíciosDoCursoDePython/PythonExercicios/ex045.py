from time import sleep
from random import randint
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
computador = randint(0, 2)
print('JO', sleep(0.5))
print('KEN', sleep(0.5))
print('PO!!!', sleep(0.5))
print('-=' * 20)

# COMPUTADOR VENCE

if computador == 1 and jogador == 0:
    print('Computador jogou Papel')
    print('Jogador jogou Pedra')
    print('-=' * 20)
    print('COMPUTADOR VENCE')
elif computador == 0 and jogador == 2:
    print('Computador jogou Pedra')
    print('Jogador jogou Tesoura')
    print('-=' * 20)
    print('COMPUTADOR VENCE')
elif computador == 2 and jogador == 1:
    print('Computador jogou Tesoura')
    print('Jogador jogou Papel')
    print('-=' * 20)
    print('COMPUTADOR VENCE')

# JOGADOR VENCE

elif jogador == 1 and computador == 0:
    print('Computador jogou Pedra')
    print('Jogador jogou Papel')
    print('-=' * 20)
    print('JOGADOR VENCE')
elif jogador == 0 and computador == 2:
    print('Computador jogou Tesoura')
    print('Jogador jogou Pedra')
    print('-=' * 20)
    print('JOGADOR VENCE')
elif jogador == 2 and computador == 1:
    print('Computador jogou Papel')
    print('Jogador jogou Tesoura')
    print('-=' * 20)
    print('JOGADOR VENCE')

#EMPATE

elif jogador == 1 and computador == 1:
    print('Computador jogou Papel')
    print('Jogador jogou Papel')
    print('-=' * 20)
    print('EMPATE')
elif jogador == 2 and computador == 2:
    print('Computador jogou Tesoura')
    print('Jogador jogou Tesoura')
    print('-=' * 20)
    print('EMPATE')
elif jogador == 0 and computador == 0:
    print('Computador jogou Pedra')
    print('Jogador jogou Pedra')
    print('-=' * 20)
    print('EMPATE')