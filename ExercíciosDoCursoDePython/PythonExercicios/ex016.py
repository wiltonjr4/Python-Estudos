''' num = float(input('Digite um número: '))
print('O número {} tem a parte inteira {:.0f}'.format(num,num)) '''

from math import trunc
num = float(input('Digite um número: '))
print('O valor de {} tem a parte inteira {}'.format(num, trunc(num)))
