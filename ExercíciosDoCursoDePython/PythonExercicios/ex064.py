cont = 0
total = 0
soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    total += 1
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a some entre eles foi {}'.format(total, soma))
