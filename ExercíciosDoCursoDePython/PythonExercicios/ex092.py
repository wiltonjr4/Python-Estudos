from datetime import date
pessoa = {}
pessoa['Nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
pessoa['Idade'] = date.today().year - nascimento
pessoa['CTPS'] = int(input('Carteira de Trabalho (0 se não tiver): '))

if pessoa['CTPS'] != 0:
    pessoa['Contratação'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = float(input('Salário: R$'))
    pessoa['Aposentadoria'] = (pessoa['Contratação'] - nascimento) + 35

print('-=' * 15)
for k, v in pessoa.items():
    print('{} tem o valor {}'.format(k, v))
