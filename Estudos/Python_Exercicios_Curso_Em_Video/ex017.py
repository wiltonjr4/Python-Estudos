from math import hypot
co = float(input('Qual é o cateto oposto?'))
ca = float(input('Qual é o cateto adjacente?'))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
