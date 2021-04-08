print('\033[35m-=\033[m' * 13)
print('\033[34mANALISADOR DE TRIÂNGULOS\033[m')
print('\033[35m-=\033[m' * 13)
n1 = float(input('Primeiro Segmento: '))
n2 = float(input('Segundo Segmento: '))
n3 = float(input('Quarto Segmento: '))
if n1 == n2 and n2 == n3 and n1 == n3:
    print('Os segmentos formarão um triângulo EQUILÁTERO!')
elif n1 == n2 or n2 == n3 or n3 == n1:
    print('Os segmentos formarão um triângulo ISÓSCELES!')
elif n1 != n2 and n2 != n3 and n3 != n1 and n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os segmentos formarão um triângulo ESCALENO!')
else: # n1 > n2 + n3 and n2 > n1 + n3 and n3 > n1 + n2:
    print('Os segmentos NÃO PODEM formar um triângulo!')
