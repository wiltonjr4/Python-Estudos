alunos = list()
notas = list()
c = 0
while True:
    alunos.append([str(input('Nome: '))])
    notas.append([float(input('Nota 1: '))])
    notas[c].append(float(input('Nota 2: ')))
    alunos[c].append((notas[c][0] + notas[c][1]) / 2)
    c += 1

    continuar = str(input('Quer continuar? ')).upper().strip()
    if continuar == 'N':
        break

print('-=' * 20)
print('N°   NOME                    MÉDIA')
print('-' * 20)
for pos, val in enumerate(range(len(alunos))):
    print(f'{pos:<8}{alunos[pos][0]:<35}{alunos[pos][1]:>}')
print('-' * 20)
while True:
    num = int(input('Montar notas de qual aluno? (999 interrompe): '))
    if num == 999:
        break
    print(f'Notas de {alunos[num][0]} são {notas[num]}')
    print('-' * 20)

