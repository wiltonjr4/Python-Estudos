lista = list()
pares = list()
impares = list()
while True:
    lista.append(int(input('Digite um número: ')))

    continuar = str(input('Quer continuar? [S/N]')).upper().strip()
    while continuar not in 'SN':
        continuar = str(input('Quer continuar?')).upper().strip()
    if continuar == 'N':
        break

for num in lista:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print('-=' * 20)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
