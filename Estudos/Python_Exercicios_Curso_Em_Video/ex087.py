matriz = [[], [], []]
for p, v in enumerate(range(0, 11)):
    if p < 3:
        matriz[0].append(int(input(f'Digite um valor para [0, {p}]: ')))
    if  p > 3 and p < 7:
        matriz[1].append(int(input(f'Digite um valor para[1,  {p-4}]: ')))
    if p > 7 and p < 11:
        matriz[2].append(int(input(f'Digite um valor para [2, {p-8}]: ')))

print('-=' * 40)
print(f'[   {matriz[0][0]}   ] [   {matriz[0][1]}   ] [   {matriz[0][2]}   ]')
print(f'[   {matriz[1][0]}   ] [   {matriz[1][1]}   ] [   {matriz[1][2]}   ]')
print(f'[   {matriz[2][0]}   ] [   {matriz[2][1]}   ] [   {matriz[2][2]}   ]')
print('-=' * 40)

par = 0
for i, c in enumerate(matriz):
    if matriz[0][i] % 2 == 0:
        par += matriz[0][i]
    if matriz[1][i] % 2 == 0:
        par += matriz[1][i]
    if matriz[2][i] % 2 == 0:
        par += matriz[2][i]

print(f'A soma dos valores pares é {par}.')

terc = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f'A soma dos valores da terceira coluna é {terc}.')

mseg = 0
if matriz[1][0] >= matriz[1][1] and matriz[1][0] >= matriz[1][2]:
    mseg = matriz[1][0]
elif matriz[1][1] >= matriz[1][2] and matriz[1][1] >= matriz[1][0]:
    mseg = matriz[1][1]
elif matriz[1][2] >= matriz[1][1] and matriz[1][2] >= matriz[1][0]:
    mseg = matriz[1][2]
print(f'O maior valor da segunda linha é {mseg}.')