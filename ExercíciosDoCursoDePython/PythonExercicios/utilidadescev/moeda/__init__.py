def metade(n=0, form=False):
    divisao = n / 2
    if form == True:
        return '{:>8}{:.2f}'.format('R$', divisao).replace('.', ',')
    return divisao


def dobro(n=0, form=False):
    multiplicacao = n * 2
    if form == True:
        return '{:>8}{:.2f}'.format('R$', multiplicacao).replace('.', ',')
    return multiplicacao


def aumentar(n=0, p=0, form=False):
    porcentomais = (p / 100 * n) + n
    if form == True:
        return '{:>8}{:.2f}'.format('R$', porcentomais).replace('.', ',')
    return porcentomais


def diminuir(n=0, p=0, form=False):
    porcentomenos = n - (p / 100 * n)
    if form == True:
        return '{:>8}{:.2f}'.format('R$', porcentomenos).replace('.', ',')
    return porcentomenos


def real(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(preco=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('                RESUMO DO VALOR')
    print('-' * 30)
    print(f'Preço analisado: {real(preco):>15}')
    print(f'Dobro do preço: {dobro(preco, True):>17}')
    print(f'Metade do preço: {metade(preco, True):>13}')
    print(f'{taxaa}% de aumento: {aumentar(preco, taxaa, True):>15}')
    print(f'{taxar}% de redução: {diminuir(preco, taxar, True):>16}')
    print('-' * 30)

