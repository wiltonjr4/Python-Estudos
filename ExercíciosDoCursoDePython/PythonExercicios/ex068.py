from random import randint
print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 15)
total = 0
soma = 0
while True:
    numjog = int(input('Diga um valor: '))
    escolhajog = str(input('Par ou Ímpar? [P/I] ')).upper().strip()
    numcomp = randint(0, 10)
    soma = numjog + numcomp

    # MOSTRANDO O RESULTADO

    if soma % 2 == 0:
        print('-' * 30)
        print(f'Você jogou {numjog} e o computador {numcomp}. Total de {soma} DEU PAR')
        print('-' * 30)
    if soma % 2 == 1:
        print('-' * 30)
        print(f'Você jogou {numjog} e o computador {numcomp}. Total de {soma} DEU ÍMPAR')
        print('-' * 30)

    # MOSTRANDO VENCEDOR

    if soma % 2 == 0 and escolhajog == 'P':
        print('Você GANHOU!')
        print('=-' * 15)
        total += 1
    if soma % 2 == 1 and escolhajog == 'I':
        print('Você GANHOU!')
        total += 1
        print('=-' * 15)
    if soma % 2 == 0 and escolhajog == 'I':
        print('Você PERDEU!')
        break
    if soma % 2 == 1 and escolhajog == 'P':
        print('Você PERDEU!')
        break

    # FINAL

print('=-' * 20)
print(f'GAME OVER! Você venceu {total} vezes.')






