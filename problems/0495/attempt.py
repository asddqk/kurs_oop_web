n = int(input())
T = []
for i in range(n):
    x, y = map(int, input().split())
    T.append([x, y])
K = int(input())
for i in range(K):
    E = []
    for l in range(n):
        x1, y1 = T[l - 1]
        x2, y2 = T[l]
        E.append([(x1+x2)/2,(y1+y2)/2])
    T=E
s = 0
if K==0:
    E=T
for l in range(n):
    x1, y1 = E[l-1]
    x2, y2 = E[l]
    s+=((x1-x2)**2+(y1-y2)**2)**0.5
print(s)