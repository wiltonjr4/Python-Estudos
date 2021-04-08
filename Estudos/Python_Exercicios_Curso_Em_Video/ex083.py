exp = str(input('Digite a expressão: '))
aberto = 0
fechado = 0
for cont in exp:
    if cont in '(':
        aberto += 1
    if cont in ')':
        fechado += 1
if aberto == fechado:
    print('Sua expressão está CORRETA!')
else:
    print('Sua expressão está ERRADA!')
