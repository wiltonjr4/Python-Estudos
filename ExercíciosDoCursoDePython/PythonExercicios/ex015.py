km = float(input('Quantos KM o seu carro alugado percorreu?'))
dias = int(input('Quantos dias você alugou?'))
custo = (dias * 60) + (km * 0.15)
print('Você percorreu {:.1f}km, por um período de {} dias. \n O valor a pagar é de: R${:.2f}'.format(km, dias, custo))

