from sys import *
setrecursionlimit(500*500+1)

n,m=map(int,input().split())
T=[list(input()) for i in range(n)]
E=0
def f(x,y):
    if T[x][y]=='#':
        T[x][y]='.'
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
        if T[i][l]=='#':
            E+=1
            f(i,l)
print(E)