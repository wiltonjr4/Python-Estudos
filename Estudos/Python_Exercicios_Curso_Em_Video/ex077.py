palavras = ('aprender', 'programar', 'curso')
for c in palavras:
    print(f'\nNa palavra {c.upper()} temos', end= ' ')
    for l in c:
        if l.lower() in 'aeiou':
            print(l, end = ' ')
