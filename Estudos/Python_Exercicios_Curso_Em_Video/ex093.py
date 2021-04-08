jogador = {}
gols = []
totalg = 0
jogador['nome'] = str(input('Nome do Jogador: '))
num = int(input('Quantas partidas {} jogou? '.format(jogador['nome'])))

for v in range(num):
    gol = int(input('Quantos gols na {}° partida? '.format(v + 1)))
    gols.append(gol)
    totalg += gol
jogador['gols'] = gols
jogador['total'] = totalg

print('-=' * 20)
print(jogador)
print('-=' * 20)

for k, v in jogador.items():
    print('O campo {} tem o valor {}.'.format(k, v))
print('-=' * 20)
print('O jogador {} jogou {} partidas.'.format(jogador['nome'], num))

for p, g in enumerate(gols):
    print('{:>10} Na {}° partida, fez {} gols.'.format('=>', p+1, g ))
print('Foi um total de {} gols.'.format(jogador['total']))
