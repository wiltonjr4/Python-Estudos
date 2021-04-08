num1 = (int(input('Digite um número: ')))
num2 = (int(input('Digite outro número: ')))
num3 = (int(input('Digite mais um número: ')))
num4 = (int(input('Digite o último número: ')))
total = num1, + num2, + num3, + num4
print(f'Você digitou os valores {total}')
print(f'O valor 9 foi apareceu {total.count(9)} vezes')
if 3 in total:
    print(f'O valor 3 apareceu na {total.index(3)+1}ª posição')
else:
    print('O valor 3 não apareceu em nenhuma posição')

# Valores pares
print(f'Os valores pares digitados foram ', end='')
for c in total:
    if c % 2 == 0:
        print(c, end=' ')

'''
# Pegando quantidade de 9
nove = 0
for c in total:
    if c == 9:
        nove += 1
print(f'O valor 9 apareceu {nove} vezes')

# Pegando posição do valor 3
for c in total:
    if c == 3:
        tres = total.index(3)
        print(f'O valor 3 apareceu na {tres+1}° posição')
    else:
        print('O valor 3 não apareceu em nenhuma posição')
        break

'''