listagem = []
pessoa = {}
media = 0
total = 0
while True:
 # PEGANDO NOME
    pessoa['nome'] = str(input('Nome: '))

 # VALIDANDO SEXO
    pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()
    while pessoa['sexo'] not in 'MF':
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()

# PEGANDO IDADE
    pessoa['idade'] = int(input('Idade: '))

# VALIDANDO CONTINUAR
    continuar = str(input('Quer continuar? [S/N]')).upper().strip()
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).upper().strip()

    listagem.append(pessoa.copy())
    if continuar == 'N':
        break

print('-=' * 20)
print(f'-  O grupo tem {len(listagem)} pessoas.')

# ESCREVE A MÉDIA DE IDADE
for p, n in enumerate(listagem):
    total += (listagem[p]['idade'])
media = total / len(listagem)
print(f'-  A média de idade é de {media} anos.')

# ESCREVE APENAS AS MULHERES
print(f'-  As mulheres cadastradas foram: ', end='')
for p, n in enumerate(listagem):
    if listagem[p]['sexo'] == 'F':
        print(listagem[p]['nome'], end='.. ')
print()

# ESCREVE AS PESSOAS ACIMA DA MÉDIA DE IDADE
print('-  Lista das pessoas que estão acima da média de idade do grupo:\n')
for p, n in enumerate(listagem):
    if listagem[p]['idade'] > media:
        print('nome = {}; sexo = {}; idade = {};'.format(listagem[p]['nome'], listagem[p]['sexo'], listagem[p]['idade']))
print('\n<<  ENCERRADO  >>')

