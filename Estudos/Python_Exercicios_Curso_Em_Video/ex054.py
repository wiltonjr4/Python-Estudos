from datetime import date
maior = int()
menor = int()
for c in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    anohoje = date.today().year
    if anohoje - ano >= 18:
        maior = maior + 1
    else:
        menor = menor +1
print('''\nAo todo tivemos {} pessoas maiores de idade
E também tivemos {} menores de idade'''.format(maior, menor))
