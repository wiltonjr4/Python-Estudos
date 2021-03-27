total = [[], []]
for p, c in enumerate(range(0, 7)):
    num = int(input(f'Digite o {p+1}° valor: '))
    if num % 2 == 0:
        total[0].append(num)
    else:
        total[1].append(num)

print(f'Os valores pares digitados foram: {sorted(total[0])}')
print(f'Os valores ímpares digitados foram: {sorted(total[1])}')


