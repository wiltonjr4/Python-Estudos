soma = 0
total = 0
while True:
    num = int(input('Digite um valor: '))
    if num == 999:
        break
    total += 1
    soma += num
print(f'A soma dos {total} foi {soma}!')
