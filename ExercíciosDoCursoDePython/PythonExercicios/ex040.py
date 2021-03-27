nota1 = float(input('Primeira Nota: '))
nota2 = float(input(' Segunda Nota: '))
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {}'.format(nota1, nota2, media))
if media >= 7.0:
    print('O aluno está \033[42mAPROVADO!\033[m')
elif media <= 5.0:
    print('O aluno está \033[41mREPROVADO\033[m')
else:
    print('O aluno está de RECUPERAÇÃO!')
