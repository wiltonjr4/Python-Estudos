from datetime import date
ano = int(input('Que ano você quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year # Pegando o ano de atual!
if ano % 4 == 0:
    print('O ano {} é BISSEXTO!'.format(ano))
    if ano % 100 == 1:
        print('O ano {} é BISSEXTO!'.format(ano))
        if ano % 400 == 0:
            print('O ano {} é BISSEXTO!'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))
