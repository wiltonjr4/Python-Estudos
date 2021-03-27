from random import randint
from time import sleep
jogadores = []
print('Valores sorteados: ')
for c in range(1, 5):
    jogador = {'nome': 'jogador {}'.format(c)}
    jogador['valor'] = randint(0, 6)
    jogadores.append(jogador.copy())
    print('     O {} tirou {}'.format(jogador['nome'], jogador['valor']))
    sleep(1)

print('Ranking dos jogadores: ')
    




