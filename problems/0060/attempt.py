n = int(input())
m = 35000
T = [i for i in range(m + 1)]
T[1] = 0
E = []
for i in range(len(T)):
    if T[i] != 0:
        x = 2
        while i * x <= m:
            T[i * x] = 0
            x += 1
    if T[i] != 0:
        E.append(i)
Key = []
for i in range(500):
    Key.append(E[E[i] - 1])
print(Key[n - 1])