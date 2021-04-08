n1 = float(input('Quantos M² de Largura Mede a Parede?'))
n2 = float(input('Quantos M² de Altura Mede a Parede?'))
area = n1*n2
litros = area/2
print('Para pintar essa parede de {:.1f}m² de área, você precisará de: {:.1f} litros de tinta'.format(area,litros))

