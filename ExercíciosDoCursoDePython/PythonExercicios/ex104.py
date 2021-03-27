def leiaInt(msg):
    n = input(msg)
    while True:
        if n.isnumeric() == False:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
            n = input(msg)
        else:
            break
    return n



n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')


