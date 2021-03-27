pessoas = list()
dados = list()
maior = menor = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()

    continuar = str(input('Quer continuar? [S/N]')).upper().strip()
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).upper().strip()
    if continuar == 'N':
        break

print('-=' * 30)
print(f'Ao todo você cadastrou {len(pessoas)}')

for i, v in enumerate(pessoas):
    if i == 0:
        maior = pessoas[i][1]
        menor = pessoas[i][1]
    elif pessoas[i][1] > maior:
        maior = pessoas[i][1]
    elif pessoas[i][1] < menor:
        menor = pessoas[i][1]
print(f'O maior peso foi {maior}KG de ', end=' ')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]}', end='  ')
print(f'\nO menor peso foi {menor}KG de ', end=' ')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]}', end=' ')
