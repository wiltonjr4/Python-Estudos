matriz = [[], [], []]
for p, v in enumerate(range(0, 11)):
    if p < 3:
        matriz[0].append(int(input(f'Digite um valor para [0, {p}]: ')))
    if  p > 3 and p < 7:
        matriz[1].append(int(input(f'Digite um valor para[1,  {p-4}]: ')))
    if p > 7 and p < 11:
        matriz[2].append(int(input(f'Digite um valor para [2, {p-8}]: ')))

print(f'[   {matriz[0][0]}   ] [   {matriz[0][1]}   ] [   {matriz[0][2]}   ]')
print(f'[   {matriz[1][0]}   ] [   {matriz[1][1]}   ] [   {matriz[1][2]}   ]')
print(f'[   {matriz[2][0]}   ] [   {matriz[2][1]}   ] [   {matriz[2][2]}   ]')


