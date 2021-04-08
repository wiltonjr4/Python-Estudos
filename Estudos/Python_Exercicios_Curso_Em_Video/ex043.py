peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m)' ))
imc = peso / (altura ** 2)
print('O seu IMC atual é de: {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO do peso normal!')
elif imc <= 25:
    print('Você está com o peso IDEAL!')
elif imc <= 30:
    print('Você está com SOBREPESO!')
elif imc <= 40:
    print('Você esta em OBESIDADE!')
else:
    print('Você está em OBESIDADE MÓRBIDA! Cuidado!')
