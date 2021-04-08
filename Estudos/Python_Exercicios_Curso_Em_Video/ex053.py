frase = str(input('Digite uma frase: ')).strip().upper()
separar = frase.split()
juntar = ''.join(separar)
inverso = ''
for letra in range(len(juntar) - 1, -1, -1):
    inverso = inverso + juntar[letra]
print('Você digitou {}, o inverso da palavra é {}'.format(frase, inverso))
if inverso == juntar:
    print('A frase é um Palíndromo')
else:
    print('A frase não é um Palíndromo')
