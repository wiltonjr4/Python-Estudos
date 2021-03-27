lista = ('Flamengo', 'Internacional', 'Atlético-MG', 'São Paulo', 'Fluminense', 'Grêmio',
         'Palmeiras', 'Santos', 'Athletico-PR', 'Bragantino', 'Ceará', 'Corinthians',  'Atlético-GO',
         'Bahia', 'Sport', 'Fortaleza', 'Vasco', 'Goiás', 'Coritiba', 'Botafogo')

while True:

    # MENU DE ESCOLHAS ESCRITO
    print('-=' * 20)
    print('''    [ 1 ] LISTA DO BRASILEIRÃO
    [ 2 ] OS 5 PRIMEIROS COLOCADOS
    [ 3 ] OS 4 ÚLTIMOS COLOCADOS
    [ 4 ] TIMES EM ORDEM ALFABÉTICA
    [ 5 ] ESCOLHA UM TIME PARA SABER A SUA POSIÇÃO NA TABELA
    [ 6 ] SAIR DO PROGRAMA''')
    print('-=' * 20)
    menu = int(input('Digite um número: '))
    print('-=' * 20)
    # FINAL DO MENU DE ESCOLHA

    # ESCOLHA E VALIDAÇÃO DO ÚSUÁRIO
    while menu <= 0 or menu > 6:
        menu = int(input('Pro favor, digite um número entre [1 e 5] : '))

    # LISTA DO BRASILEIRÃO POR POSIÇÃO Nª1
    if menu == 1:
        print('A lista de posíções do Braslieirão é..')
        pos = 0
        for c in lista:
            pos += 1
            print(f'{pos}°{c}')

    # OS 5 PRIMEIROS COLOCADOS N°2
    if menu == 2:
        print('Os 5 primeiro colocados são..')
        pos = 0
        for c in lista[0:5]:
            pos += 1
            print(f'{pos}°{c}')

    # OS 4 ÚLTIMOS SÃO N° 3
    if menu == 3:
        print('Os 4 últimos colocados são..')
        pos = 16
        for c in lista[-4:]:
            pos += 1
            print(f'{pos}°{c}')

    # TIMES EM ORDEM ALFABÉTICA N° 4
    if menu == 4:
        print('Times em ordem alfabética', sorted(lista))

    # ESCOLHA UM TIME N°5
    if menu == 5:
        num = int(input('Digite uma posíção: '))
        while num < 0 or num > 20:
            posicao = int(input('Pro favor, gigite uma posíção entre 1 e 20: '))
        print(f'O time {lista[num]} esta na {num}° posição')

    # ENCERRA O PROGRAMA N°6
    if menu == 6:
        break
print('Obrigado!Volte Sempre.')


