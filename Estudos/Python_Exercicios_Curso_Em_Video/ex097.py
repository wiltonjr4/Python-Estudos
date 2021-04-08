def escreva():
    txt = str(input('Digite um texto: '))
    acento = '~' * (len(txt) + 4)
    print(acento)
    print(f'  {txt}')
    print(acento)


escreva()
