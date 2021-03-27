from datetime import datetime
ano = int(input('Ano de nascimento: '))
idade = datetime.now().year - ano
anoatual = datetime.now().year
print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, anoatual))
if idade < 18:
    print('Ainda faltam {} anos para o alistamento'.format(18 - idade))
    print('Seu alistamento será em {}'.format(anoatual + (18 - idade)))
elif idade > 18:
    print('Você ja deveria ter se alistado há {} anos'.format(idade - 18))
    print('O seu alistamento foi em {}'.format(anoatual - (idade - 18)))
else:
    print('Você tem que se alistar IMEDIATAMENTE!')
