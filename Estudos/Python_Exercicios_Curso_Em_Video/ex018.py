import math
an = float(input('Digita o ângulo que você deseja: '))
seno = math.sin(math.radians(an))
cosseno = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print('O ângulo {} tem, SENO = {:.2f}, COSSENO = {:.2f} e TANGETE = {:.2f}'.format(an, seno, cosseno, tan))


