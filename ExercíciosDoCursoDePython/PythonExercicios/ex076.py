lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo',
         25.00, 'Tranferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32,
         'Canetas', 22.30, 'Livro', 34.90)
print('-' * 20)
print(f'LISTAGEM DE PREÇO')
print('-' * 20)
for c in lista:
    if type(c) == str:
        print(f'{c:.<30}', end=' ')
    if type(c) == float:
        print(f'R${c:.2f}')
print('-' * 20)
