n = int(input())
T = {}
for i in range(n):
    a, b = map(int, input().split())
    if a in T:
        T[a] += 1
    else:
        T[a] = 1
    if b in T:
        T[b] -= 1
    else:
        T[b] = -1
LEN = 0
k = 0
T = sorted([i, T[i]] for i in T)
for i in range(len(T)-1):
    k += T[i][1]
    if k > 0:
        LEN += T[i + 1][0] - T[i][0]
print(LEN)