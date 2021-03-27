aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Média de {}: '.format(aluno['nome'])))
print('Nome é igual a {}'.format(aluno['nome']))
print('Média igual a {}'.format(aluno['media']))
if aluno['media'] >= 7:
    print('A situação é Aprovado')
else:
    print('A situação é Reprovado')
