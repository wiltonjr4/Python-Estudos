from time import sleep


def contador(i, f, p):
    if p < 0:
        p = abs(p)
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    while i < f or i > f:
        if i < f:
            while i < f+1:
                print(f'{i}', end='  ')
                i += p
                sleep(0.4)
            break
        if i > f:
            while i > f-1:
                print(f'{i}', end='  ')
                i -= p
                sleep(0.4)
            break
    print('FIM!')


def linha():
    print('-=' * 15)


contador(1, 10, 1)
contador(10, 0, 2)
linha()
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)


