a, b = map(int, input().split())
R = []
for n in range(a, b + 1):
    i = 2
    c = 0
    while i <= n ** 0.5:
        if n % i == 0:
            c += 1
            break
        else:
            i += 1
    if c == 0:
        R.append(n)
L = []
R = R[::-1]
for i in range(len(R)):
    L.append(sum([int(l) for l in str(R[i])]))
try:
    if R[L.index(max(L))]==1:
        c=8/0
    print(R[L.index(max(L))])
except:
    print(-1)