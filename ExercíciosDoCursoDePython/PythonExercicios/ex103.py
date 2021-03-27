def ficha(nome='<desconhecido>', gols=0 ):
    nome = str(input('Nome do Jogador: '))
    gols = int(input('Número de Gols: '))
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


ficha()

