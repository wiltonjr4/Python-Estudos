print('-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-')
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-')
from random import randint # Comando para Gerar números Aleatórios
from time import sleep # Comando para deixar o computador "PROCESSANDO"
lista = randint(0, 5) # Faz o computador "pensar"
num = int(input('Em que número eu pensei? ')) # Jogador tenta advinhar
print('PROCESSANDO...')
sleep(2)
if num == lista:
    print('PARABÈNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(lista, num))



