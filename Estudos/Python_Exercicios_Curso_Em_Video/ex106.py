def ajuda():
    while True:
        print('\033[46m~' * 26)
        print('    SISTEMA DE AJUDA PyHELP')
        print('~' * 26)
        ususario = str(input('\033[mFunção ou Biblioteca > ')).strip().lower()
        if ususario == 'fim':
            print('\033[41mENCERRANDO... Volte sempre!')
            break
        tio = '\033[42m~' * (len(ususario) + 32)
        print(tio)
        print(f'    Acessando o manual do comando "{ususario}"')
        print(tio)
        print('\033[m')
        help(ususario)


ajuda()

