lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))

    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()
    while continuar not in 'SN':
        continuar = str(input('Tente novamente.. Quer continuar? [S/N] ')).upper().strip()

    if continuar == 'N':
        break

print('-=' * 20)
print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são {sorted(lista, reverse=True)}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 Não faz parte da lista!')
