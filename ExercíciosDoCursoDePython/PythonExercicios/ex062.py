print('Gerador de PA')
print('-=' * 10)
termo = int(input('Primtiro termo: '))
razao = int(input('Razão da PA: '))
cont = 0
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        print('{}  >  '.format(termo), end=' ')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você que mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
