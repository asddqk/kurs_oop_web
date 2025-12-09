from functools import lru_cache


@lru_cache(None)
def F(n, k, c, x, y):
    if k == 0:
        if x == n and y == n:
            return 1
        else:
            return 0
    else:
        h = []
        if T[x][y - 1] == '0':
            h.append(F(n, k - 1, c, x, y - 1))
        if T[x][y + 1] == '0':
            h.append(F(n, k - 1, c, x, y + 1))
        if T[x - 1][y] == '0':
            h.append(F(n, k - 1, c, x - 1, y))
        if T[x + 1][y] == '0':
            h.append(F(n, k - 1, c, x + 1, y))
        return c + sum(h)


N, K = map(int, input().split())
T = []
T.append(['1'] * (N + 2))
for lol in range(N):
    T.append(['1'] + list(input()) + ['1'])
T.append(['1'] * (N + 2))
print(F(N, K, 0, 1, 1))