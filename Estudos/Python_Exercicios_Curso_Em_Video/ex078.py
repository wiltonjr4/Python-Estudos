num = list()
maior = list()
menor = list()
for cont in range(0, 5):
    num.append(int(input(f'Digite um valor para a Posição {cont}: ')))
for i, v in enumerate(num):
    if v == max(num):
        maior.append(i)
    if v == min(num):
        menor.append(i)
print('-=' * 20)
print(f'Você digitou os valores{num}')
print(f'O maior valor foi {max(num)} nas posições {maior}')
print(f'O menor valor foi {min(num)} na posição {menor}')
