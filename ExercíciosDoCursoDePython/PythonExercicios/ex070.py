somapreco = 0
maisdemil = 0
maisbarato = 0
nomebarato = ' '
cont = 0
print('-' * 20)
print('LOJA SUPER BARATÃO')
print('-' * 20)
while True:
    nome = str(input('Nome do Produto: ')).upper().strip()
    preco = float(input('Preço: R$'))
    somapreco += preco
    if preco >= 1000:
        maisdemil += 1
    if cont == 0:
        maisbarato = preco
        nomebarato = nome
    if cont >= 1:
        if preco < maisbarato:
            maisbarato = preco
            nomebarato = nome
    cont += 1
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()
    if continuar == 'N':
        break
print(f'O total da compra foi R${somapreco:.2f}')
print(f'Temos {maisdemil} custando mais de R$1000.00')
print(f'O produto mais barato foi {nomebarato} que custa R${maisbarato:.2f}')

