# COMPUTADOR JOGOU
from random import randint
comp = randint(0, 10)
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue advinhar qual foi?''')
print(comp)
# PESSOA VAI JOGAR
cont = 0
pessoa = int(input('Qual é o seu palpite? '))
# VALIDANDO RESULDADO
while pessoa != comp:
    cont += 1
    if comp > pessoa:
        print('Mais.. Tente mais uma vez.')
        pessoa = int(input('Qual é o seu palpite? '))
    else:
        print('Menos.. Tente mais uma vez.')
        pessoa = int(input('Qual é o seu palpite? '))
#FINAL
print('Acertou com {} tentativas. Parabéns!'.format(cont + 1))
