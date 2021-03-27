idade = 0


def eleicao(nascimento):
    from datetime import date
    global idade
    idade = date.today().year - nascimento
    if idade >= 18 or idade < 65:
       voto = 'VOTO OBRIGATÓRIO.'
    if idade < 18:
        voto = 'NÃO VOTA.'
    if idade >= 65:
        voto = 'VOTO OPCIONAL.'
    return voto


resu = eleicao(int(input('Em que ano você nasceu?')))
print(f'Com {idade} anos: {resu}')


