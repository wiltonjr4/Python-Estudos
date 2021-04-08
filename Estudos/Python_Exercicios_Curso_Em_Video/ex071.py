valor = int(input('Que valor você quer sacar? R$ '))
ced = 50
totalced = 0
while True:
    if valor >= ced:
        valor -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced =1
        totalced = 0
        if valor == 0:
            break

