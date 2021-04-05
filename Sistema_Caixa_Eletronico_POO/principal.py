from sistema_OO import conta
from random import randint

print('-=' * 9)
print('CAIXA ELETRÔNICO')
print('-=' * 9)
print('''\033[34m[ 1 ] ABRIR NOVA CONTA\033[m
\033[34m[ 2 ] ACESSAR CONTA\033[m
\033[34m[ 0 ] ENCERRAR PROGRAMA\033[m''')
print('-=' * 9)
num = int(input('Digite um número: '))
print('-=' * 9)

if num == 1:
    titular = str(input('Digite um nome para o TITULAR da conta: '))
    numero_conta = []
    for number in range(0, 7):
        numero_conta.append(randint(0, 9))
    conta = conta(titular, numero_conta, saldo=0)
    print(f'Conta criada com sucesso.. Títular: {titular}, N° da Conta: ', end='')
    for dig in numero_conta:
        print(dig, end='')
    print(', Saldo = R$0,0')

if num == 2:
    print('-=' * 9)
    print('CAIXA ELETRÔNICO')
    print('-=' * 9)
    print(f'Conta de {conta.nome}, N°: {conta.numero}')
    print('-=' * 9)
    print('''\033[34m[ 1 ] EXTRATO\033[m
    \033[34m[ 2 ] SACAR\033[m
    \033[34m[ 3 ] DEPOSITAR\033[m
    \033[34m[ 4 ] TRANSFERIR\033[m
    \033[34m[ 0 ] ENCERRAR PROGRAMA\033[m''')
    print('-=' * 9)








