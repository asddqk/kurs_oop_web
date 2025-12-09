n = int(input())
R = list(map(int, input().split()))
i = 2
T = []
while i * i < 10 ** 9 + 1:
    n = 2
    while i ** n < 10 ** 9 + 1:
        T.append(i ** n)
        n += 1
    i += 1
for n in R:
    if n in T:
        print('YES')
    else:
        print('NO')