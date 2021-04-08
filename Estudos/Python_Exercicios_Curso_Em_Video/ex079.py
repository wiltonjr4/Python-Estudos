lista = list()
while True:
    num = int(input('Digite um valor: '))
    if num in lista:
        print('Valor duplicado! Não vou adicionar...')
    else:
        lista.append(num)
        print('Valor adicionado com sucesso..')

    # VERIFICADOR
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()

    if continuar == 'N':
        break
print(f'Você digitou os valores {sorted(lista)}')

