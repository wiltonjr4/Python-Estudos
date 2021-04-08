distancia = float(input('Qual será a distância da viagem? '))
print('Você está prestes a começar uma viagem de {}Km'.format(distancia))
if distancia <= 200:
    pass1 = distancia * 0.5
    print('E o preço da sua passagem será de R${:.2f}'.format(pass1))
else:
    pass2 = distancia * 0.45
    print('E o preço da sua passagem será de R${:.2f}'.format(pass2))
