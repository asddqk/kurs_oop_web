n, m = 8,8
T = [list(input()) for i in range(n)]
E = 0
def f(x, y, c):
    if T[x][y] == c:
        if c=='W':
            c='B'
        else:
            c='W'
        T[x][y] = '.'
        if x != 0:
            f(x - 1, y,c)
        if x != n - 1:
            f(x + 1, y,c)
        if y != 0:
            f(x, y - 1,c)
        if y != m - 1:
            f(x, y + 1,c)


for i in range(n):
    for l in range(m):
        if T[i][l] in 'BW':
            E += 1
            f(i, l,T[i][l])
print(E)