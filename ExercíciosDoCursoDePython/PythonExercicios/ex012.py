n1 = float(input('Qual o valor do produto? R$'))
desc1 = n1*0.05
desc2 = n1-desc1
print('O valor do produto é: {} \n Mas na promoção com 5% de desconto, ele fica por: {:.2f}'.format(n1, desc2))

