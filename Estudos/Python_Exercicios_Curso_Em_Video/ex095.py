listagem = []
jogador = {}
gols = []
cont = 0
while True:
    print('-' * 30)
    jogador['nome'] = str(input('Nome do Jogador: '))
    num = int(input('Quantas partidas {} jogou? '.format(jogador['nome'])))

    for v in range(num):
        gols.append(int(input('Quantos gols na {}° partida? '.format(v + 1))))
        jogador['gols'] = gols[:]
    gols.clear()

    totalg = 0
    for c in jogador['gols']:
        totalg += c
    jogador['total'] = totalg

    listagem.append(jogador.copy())
    continuar = str(input('Quer continuar? [S/N]')).upper().strip()
    if continuar == 'N':
        break
    cont += 1

print('-=' * 15)
print('{:<}  {:<10} {:<10} {:<10}'.format('cod', 'nome', 'gols', 'total'))
print('-' * 30)
for k, v in enumerate(listagem):
    print('{} {:>10}       {} {:^8}'.format(k, listagem[k]['nome'], listagem[k]['gols'], listagem[k]['total']))
print('-' * 30)

while True:
    cod = int(input('Mostrar dados de qual jogador? (999 para encerrar)'))
    if cod == 999:
        break
    if cod > len(listagem):
        print('ERRO! Não existe jogador com código {}! Tente novamente'.format(cod))
    else:
        print('--  LEVANTAMENTO DO JOGADOR {}:'.format(listagem[cod]['nome']))
        for p, g in enumerate(listagem):
            print('{:>10} Na {}° partida, fez {} gols.'.format('=>', p+1, listagem[cod]['gols'][p]))
        print('-' * 30)

print('<<  VOLTE SEMPRE  >>')



