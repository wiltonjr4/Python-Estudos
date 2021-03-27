num1 = float(input('Primeiro Valor: '))
num2 = float(input('Segunda Valor: '))
num3 = float(input('Terceiro Valor: '))
if num1 > num2 and num1 > num3:
    print('O maior valor digitado foi {}'.format(num1))
if num2 > num1 and num2 > num3:
    print('O maior valor digitado foi {}'.format(num2))
if num3 > num1 and num3 > num2:
    print('O maior valor digitado foi {}'.format(num3))
if num1 < num2 and num1 < num3:
    print('O menor valor digitado foi {}'.format(num1))
if num2 < num1 and num2 < num3:
    print('O menor valor digitado foi {}'.format(num2))
if num3 < num2 and num3 < num1:
    print('O menor valor digitado foi {}'.format(num3))
