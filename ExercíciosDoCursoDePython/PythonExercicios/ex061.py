print('Gerador de PA')
print('-=' * 10)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
#pa = termo * razao
cont = 0
while cont < 10:
    print('{}  >  '.format(termo), end=' ')
    termo += razao
    cont += 1
print('FIM')

