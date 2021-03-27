from time import sleep
from random import randint
print('-' * 20)
print(f'JOGA NA MEGA SENA')
print('-' * 20)

num = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-=   SORTEANDO {num} JOGOS -=-=-=')
sleep(0.5)
for i, c in enumerate(range(num)):
    lista = [randint(0, 60), randint(0, 60), randint(0, 60),
             randint(0, 60), randint(0, 60), randint(0, 60)]
    print(f'Jogo {i+1}: {lista}')
