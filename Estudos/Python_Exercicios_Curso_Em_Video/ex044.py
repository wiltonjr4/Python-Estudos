import math
print('=' * 10, 'LOJAS GUANABARA', '=' * 10)
preco = float(input('Preço das compras: R$ '))
print('''FORMA DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
forma = int(input('Qual é a opção? '))
if forma == 1:
    total = preco - (preco * 0.1)
elif forma == 2:
    total = preco - (preco * 0.05)
elif forma == 3:
    total = preco
    parcela = preco / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif forma == 4:
    total = preco + (preco * 0.2)
    parcela = int(input('Quantas vezes no cartão? '))
    print('Sua compra sera parcelada em {}x de R${:.2f}'.format(parcela, total / parcela))
else:
    total = preco
    print('Forma de pagamento INVÁLIDA, por favor, tente novamente..')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))



