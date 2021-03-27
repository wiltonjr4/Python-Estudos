def leiaInt(msg):
    validador = False
    while not validador:
        n = str(input(msg)).strip()
        if n.isalpha() == True :
            print('\033[31mERRO! Digite um número válido. \033[m')
        elif n == '':
            n = 0
            return n
        else:
            validador = True
            return int(n)


def leiaFloat(msg):
    validador = False
    while not validador:
        n = str(input(msg)).strip()
        if n.isalpha() == True :
            print('\033[31mERRO! Digite um número válido. \033[m')
        elif n == '':
            n = 0
            return n
        else:
            validador = True
            return float(n)


try:
    i = leiaInt('Digite um número Inteiro: ')
    f = leiaFloat('Digite um número Real: ')
except (KeyboardInterrupt):
    print('Usuário preferiu não digitar esse número.')
else:
    print(f'Valor Inteiro digitado foi: {i}')
    print(f'Valor Real digitado foi: {f}')
