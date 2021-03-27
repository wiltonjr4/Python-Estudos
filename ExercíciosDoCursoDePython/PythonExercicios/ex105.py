def notas(*num, sit=False):
    '''
    Digite as notas para ter uma listagem do aluno
    :param num:Digite várias notas com ',' dividindo elas
    :param sit:digite 'True' para ter a situação do aluno
    :return:retorna a lista completa com maior, menor e media
    '''
    lista = {}
    lista['total'] = len(num)
    lista['maior'] = max(num)
    lista['menor'] = min(num)
    lista['media'] = sum(num) / lista['total']
    if sit == True:
        if lista['media'] > 7:
            lista['situação'] = 'BOA'
        elif lista['media'] >= 6 and lista['media'] < 7:
            lista['situação'] = 'RAZOÁVEL'
        else:
            lista['situação'] = 'RUIM'
    return lista


resp = notas(5.5, 9.5, 10, 4, sit=True)
print(resp)
help(notas)

