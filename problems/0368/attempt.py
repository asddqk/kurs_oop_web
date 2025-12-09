n=int(input())
T=[]
E=[]
for i in range(n):
    x=[]
    for k in input():
        x.append(int(k))
    T.append(x)
for i in range(1,n):
    T[i][0]+=T[i-1][0]
for i in range(1,n):
    T[0][i]+=T[0][i-1]
for i in range(1,n):
    for l in range(1, n):
        T[i][l]= min(T[i][l-1]+T[i][l],T[i-1][l]+T[i][l])
p=[]
x,y=n-1,n-1
while 1:
    if x==0 and y==0:
        break
    if x==0 or y==0:
        if x==0:
            y-=1
        else:
            x-=1
    else:
        if T[x-1][y]<=T[x][y-1]:
            x-=1
        else:
            y-=1
    p.append([x,y])
r=[['.']*n for i in range(n)]
for i in p:
    r[i[0]][i[1]]='#'
r[n-1][n-1]='#'
for i in r:
    print(*i,sep='')