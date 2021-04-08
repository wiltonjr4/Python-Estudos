nascimento = int(input('Ano de nascimento: '))
from datetime import date
atual = date.today().year # Pegando o Ano ATUAL
idade = atual - nascimento
print('A idade do Atleta é de {} anos'.format(idade))
if idade <= 9:
    print('A classificação é MIRIM')
elif idade <= 14:
    print('A classificação é INFANTIL')
elif idade <= 19:
    print('A classificação é JUNIOR')
elif idade <= 25:
    print('A classificação é SÊNIOR')
elif idade > 25:
    print('A classificação é MASTER')
