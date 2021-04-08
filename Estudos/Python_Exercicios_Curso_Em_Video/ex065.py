cond = 'S'
total = 0
maior = 0
menor = 0
media = 0
while cond != 'N':
    total += 1
    num = int(input('Digite um número: '))
    media += num
    cond = str(input('Quer continuar? [S/N] ')).strip().upper()
    if num > maior:
        maior = num
        menor = menor
    else:
        maior = maior
        menor = num
media /= total
print('Você digitou {} números e a média foi {}'.format(total, media))
print('O maior valor foi {} e o menos foi {}'.format(maior, menor))

