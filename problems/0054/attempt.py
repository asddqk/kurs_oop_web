n,m=map(int,input().split())
T=[list(map(int,input().split())) for i in range(n)]
E=[]
for i in T:
    E.append(min(i))
print(max(E),end=' ')
R=[]
for i in range(m):
    Q=[]
    for l in range(n):
        Q.append(T[l][i])
    R.append(max(Q))
print(min(R))