nome = str(input('Digite o seu nome completo: ')).strip()
print('Analisando o seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
nomed = nome.split()
nomec = ''.join(nomed)
print('Seu nome tem ao todo {} letras'.format(len(nomec)))
print('Seu primeiro nome é {} e ele tem {} letras'.format(nomed[0], len(nomed[0])))


