from time import sleep
primeiro = int(input('Primeiro valor: '))
segundo = int(input('Segundo valor: '))
print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] O maior
    [ 4 ] Novos números
    [ 5 ] Sair do Programa''')
sair = False
while not sair:
    escolha = int(input('>>>>> Qual é a sua opção? '))
    lista = [1, 2, 3, 4, 5]
    if escolha not in lista:
        print('Opção inválida. Tente novamente..')
    if escolha == 1:
        soma = primeiro + segundo
        print('A soma entre {} + {} é {}'.format(primeiro, segundo, soma))
        print('=-' * 20)
    if escolha == 2:
        mult = primeiro * segundo
        print('A multiplicação entre {} x {} é {}'.format(primeiro, segundo, mult))
        print('=-' * 20)
    if escolha == 3:
        if primeiro > segundo:
            print('O número {} é maior que {}'.format(primeiro, segundo))
            print('=-' * 20)
        else:
            print('O número {} é maior que {}'.format(segundo, primeiro))
            print('=-' * 20)
    if escolha == 4:
        primeiro = int(input('Primeiro valor: '))
        segundo = int(input('Segundo valor: '))
    if escolha == 5:
        sair = True
        print('=-' * 20)
    sleep(1)
print('Programa Encerrado!')
