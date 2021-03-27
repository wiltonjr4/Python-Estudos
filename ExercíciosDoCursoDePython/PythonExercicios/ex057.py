sexo = str(input('Informe seu sexo: [M/F] ')).upper().strip()
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: [M/F] ')).upper().strip()
print('Sexo {} registrado com sucesso!'.format(sexo))
