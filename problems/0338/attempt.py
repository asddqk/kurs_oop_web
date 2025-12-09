n,m=map(int,input().split())
T=[list(map(int,input().split())) for i in range(n)]
E=0
def f(x,y):
    if T[x][y]==0:
        T[x][y]=1
        if x!=0:
            f(x-1,y)
        if x!=n-1:
            f(x+1,y)
        if y!=0:
            f(x,y-1)
        if y!=m-1:
            f(x,y+1)
for i in range(n):
    for l in range(m):
        if T[i][l]==0:
            E+=1
            f(i,l)
print(E)