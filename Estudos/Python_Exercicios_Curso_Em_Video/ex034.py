salario = float(input('Digite o seu salário: '))
if salario > 1250.00:
    aumento = (salario * 0.10)
    print('PARABÈNS! Você recebeu um aumento de R${:.2f}! Seu salário total será R${:.2f}'.format(aumento, salario+aumento))
else:
    aumento = (salario * 0.15)
    print('PARABÉNS! Você recebeu um aumento de R${:.2f}! Seu salário total será R${:.2f}'.format(aumento, salario+aumento))
