import arquivo


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mOps! Opção inválida.. Tente Novamente..\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def cabecalho(lista=0, msg=''):
    if lista > 0:
        lista = print('-' * 40)
        return lista
    if msg != '':
        print('-' * 40)
        print(f'{msg.center(70)}')
        print('-' * 40)


def menu():
    while True:
        cabecalho(msg='MENU PRINCIPAL')
        print('\033[31m1-  \033[m \033[34mVer pessoas cadastradas\033[m')
        print('\033[31m2- \033[m \033[34m Cadastar nova pessoa\033[m')
        print('\033[31m3- \033[m \033[34m Sair do Sistema\033[m')
        cabecalho(40)
        opcao = leiaInt('\033[31mSua Opção: \033[m')

        if opcao == 1:
            cabecalho(msg='OPÇÃO 1')
            arquivo.leiaArquivo('listagemDePessoas')
        elif opcao == 2:
            cabecalho(msg='OPÇÃO 2')
            cadastro()
        elif opcao == 3:
            cabecalho(msg='OPÇÃO 3')
            cabecalho(msg='PROGRAMA ENCERRADO!')
            break


def cadastro():
    nome = str(input('Nome: '))
    idade = leiaInt('Idade: ')
    arquivo.cadastrar('listagemDePessoas', nome, idade)
