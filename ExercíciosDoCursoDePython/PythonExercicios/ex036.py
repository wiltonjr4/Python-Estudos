valorcasa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = float(input('Quantos anos de financiamento? '))
financiamento = valorcasa / (anos * 12)
print('Para pagar uma casa de R${:.2f} em {:.1f} anos a prestação será de R${:.2f}'.format(valorcasa, anos, financiamento))
porc = salario * 0.3
if financiamento <= porc:
    print('Emprestimo \033[30;42mCONCEDIDO!\033[m')
else:
    print('Emprestimo \033[30;41mNEGADO!\033[m')
