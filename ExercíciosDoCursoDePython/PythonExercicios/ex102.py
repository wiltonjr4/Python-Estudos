def fatorial(n, show=False):
    f = 1
    if show == False:
        for c in range(n, 0, -1):
            f *= c
        return f
    else:
        print(f'{n}', end=' ')
        for c in range(n, 0, -1):
            f *= c
            print(f' x  {c}', end=' ')
        print(f'= ', end='')
        return f


print(fatorial(5))



