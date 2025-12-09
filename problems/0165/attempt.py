from functools import  *


n,m=map(int,input().split())
T=[]
for i in range(n):
    T.append(list(map(int,input().split())))
    
@lru_cache(None)
def f(x,y,c):
    if c==0:
        if [x, y] == [m - 1, n - 1]:
            return 1
        if T[y][x]==0:
            return 0
        return f(x,y,T[y][x])
    if [x, y] == [m - 1, n - 1]:
        return 0
    if x==m-1:
        if y+c<=n-1:
            return f(x,y+c,0)
        else:
            return 0
    if y==n-1:
        if x+c<=m-1:
            return f(x+c,y,0)
        else:
            return 0
    if x+c<=m-1 or y+c<=n-1:
        if x+c<=m-1 and not y+c<=n-1:
            return f(x + c, y, 0)
        if not x+c<=m-1 and y+c<=n-1:
            return f(x,y+c,0)
        return f(x,y+c,0)+f(x+c,y,0)
    return 0
print(f(0,0,0))