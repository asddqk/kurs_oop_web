n=int( input())
T=[]
for i in range(n):
    s=list(map(int,input().split()))
    X=[]
    for i in s:
        if i==-1:
            i=10**20
        X.append(i)
    T.append(X)
for Round in range(n):
    E = [[0] * n for i in range(n)]
    for i in range(n):
        for l in range(n):
            E[i][l]=min(T[i][l],T[Round][l]+T[i][Round])
    T=E
z=0
for i in range(n):
    for l in range(n):
        if T[i][l]!=10**20:
            z=max(z,T[i][l])
if z==10**20:
    print(0)
else:
    print(z)