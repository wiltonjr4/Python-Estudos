conthomem = 0
contmulher = 0
mais18 = 0
while True:

    # PEGANDO VALORES
    print('-' * 20, '\nCADASTRE UMA PESSOA\n', '-' * 20)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ')).strip().upper()

    # TESTADOR RESPOSTA
    while sexo not in 'FM':
        sexo = str(input('Sexo: ')).strip().upper()

    # CONTABILIZANDO NÚMEROS
    if sexo == 'M':
        conthomem += 1
    if sexo == 'F' and idade <= 20:
        contmulher += 1
    if idade >= 18:
        mais18 += 1

    # VALIDAÇÃO QUERER CONTINUAR OU ENCERRAR O PROGRAMA
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] '))
    if continuar == 'N':
        break

    # MOSTRANDO ESTATÍSTICAS
print('=' * 10, '  FIM DO PROGRAMA  ', '=' * 10)
print(f'Total de pessoas com mais de 18 anos: {mais18}')
print(f'Ao todo temos {conthomem} cadastrados')
print(f'E temos {contmulher} mulheres com menos de 20 anos')
