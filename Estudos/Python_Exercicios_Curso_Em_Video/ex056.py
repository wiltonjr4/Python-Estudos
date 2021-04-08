idademedia = float(0)
homemvelho = 0
nomehomem = ''
mulheresnovas = 0
for p in range(1, 5):
    print('-' * 5, ' {}ª PESSOA '.format(p), '-' * 5)
    # PEGA O NOME
    nome = str(input('Nome: ')).strip()
    #PEGA A IDADE
    idade = int(input('Idade: '))
    idademedia += idade
    # PEGAR O SEXO
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    if sexo == 'F':
        if idade < 20:
            mulheresnovas += + 1
    elif sexo == 'M':
        if p == 1:
            homemvelho = idade
        else:
            if idade > homemvelho:
                homemvelho = idade
                nomehomem = nome
            if idade < homemvelho:
                homemvelho = homemvelho
       #ENCERRA O LOOP
idademedia = idademedia / 4
print('A média de idade do grupo é de {} anos'.format(idademedia))
print('O homem mais velho tem {} anos e se chama {}'.format(homemvelho, nomehomem))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulheresnovas))
