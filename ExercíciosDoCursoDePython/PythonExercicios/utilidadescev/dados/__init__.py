def leiaDinheiro(msg):
    validador = False
    while not validador:
        num = str(input(msg).strip()).replace(',', '.')
        if num.isalpha():
            print(f'\033[31m"{num}" não é um número válido\033[m')
        elif num == '':
            print(f'\033[31m"{num}" não é um número válido\033[m')
        elif num in ',':
            validador = True
            return float(num)
        else:
            validador = True
            return float(num)

