from sistema_OO import conta
from random import randint
contas = []

while True:
    print('-=' * 9)
    print('CAIXA ELETRÔNICO')
    print('-=' * 9)
    print('''           \033[34m[ 1 ] ABRIR NOVA CONTA\033[m
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
        contas.append(conta(titular, numero_conta, saldo=0))
        print(f'\033[32mConta criada com sucesso.. Títular: {titular}, N° da Conta: ', end='')
        for dig in numero_conta:
            print(dig, end='')
        print(', Saldo = R$0,0\033[m')

    if num == 2:
        while True:
            for index, pessoa in enumerate(contas):
                print(f' \033[31mDigite {index} Para Acessar a conta de {pessoa.nome} ')
                print('-=' * 9)
            numcont = int(input('\033[mDigite um número: '))
            break

        while True:
            print('-=' * 9)
            print(f'\033[32mConta de {contas[numcont].nome}, N°: {contas[numcont].numero}\033[m')
            print('-=' * 9)
            print('''            \033[34m[ 1 ] EXTRATO\033[m
            \033[34m[ 2 ] SACAR\033[m
            \033[34m[ 3 ] DEPOSITAR\033[m
            \033[34m[ 4 ] TRANSFERIR\033[m
            \033[34m[ 0 ] SAIR DA CONTA\033[m''')
            print('-=' * 9)
            dig = int(input('Digite um número: '))

            if dig == 1:
                print('-=' * 9)
                print(f'Seu \033[31mSALDO\033[m atual é de: \033[31mR${contas[numcont].extrato:.2f}\033[m')

            if dig == 2:
                valor = int(input('Qual valor você deseja \033[31mSACAR?\033[m R$ '))
                contas[numcont].set_sacar(valor)
                print('Saque efetuado com \033[34SUCESSO!\033[m')

            if dig == 3:
                valor = int(input('Qual valor você deseja \033[31mDEPOSITAR\033[m? R$'))
                contas[numcont].set_depositar(valor)
                print('Deposito efetuado com\033[34m SUCESSO!\033[m')

            if dig == 4:
                valor = int(input('Qual valor você deseja \033[31mTRANSFERIR?\033[m R$'))
                for index, pessoa in enumerate(contas):
                    if index != numcont:
                        print(f' \033[31mPara a conta de {pessoa.nome}, digite [ {index} ]  ')
                destinoNome = int(input('\033[mPara QUEM você deseja realizar essa \033[34mTRANSFERÊNCIA?\033[m (DIGITE O NÚMERO) '))
                destino = contas[destinoNome]
                contas[numcont].set_tranferir(valor, destino)
                print('\033[34mTRANSFERÊNCIA\033[m realizada com \033[34mSUCESSO!\033[m')

            if dig == 0:
                break

    if num == 0:
        print('\033[31mPrograma Encerrado. Volte Sempre!\033[m')
        break







