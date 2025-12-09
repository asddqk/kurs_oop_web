n, k = map(int, input().split())
T = sorted(list(map(int, input().split())))
if len(T) > n:
    i = len(T) - 1
    while len(T) > n:
        T.pop(i)
        i -= 1
T = T[::-1]
SUM = 0
for i in range(len(T)):
    SUM += (1 + i // k) * T[i]
print(SUM)