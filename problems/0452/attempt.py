T = [1, 2]
for i in range(350):
    T.append(sum(T[i:i + 2]))


def S(b):
    return sum([int(b[-1 - i]) * T[i] for i in range(len(b))])

d=input
SUM = S(d()) + S(d())
e = ''
for i in range(352):
    g = T[-1 - i]
    U = g <= SUM
    if U:
        SUM -= g
    e += f'{int(U)}'
print(int(e))