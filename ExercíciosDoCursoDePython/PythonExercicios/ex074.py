from random import randint
num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10) )
print(f'Os valores sorteados foram: {num}')
'''
maior = 0
menor = 0
  for c in num:
    if maior == 0:
        maior = c
    if maior < c:
        maior = c
    if menor == 0:
        menor = c
    if c < menor:
        menor = c

'''
print(f'O maior valor sorteado foi {max(num)}')
print(f'O menor valor sorteado foi {min(num)}')

