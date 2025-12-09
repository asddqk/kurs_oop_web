n=int(input())
T=[list(map(int,input().split())) for i in range(n)] 
P=sum([sum(T[i]) for i in range(n)])//2
while 1:
    E=[sum(T[i]) for i in range(n)]
    if 1 in E:
        c=E.index(1)
    else:
        break
    for i in range(n):
        T[c][i]=0
        T[i][c]=0
E=[sum(T[i]) for i in range(n)]
if min(E)==max(E) and min(E)==0 and P==n-1:
    print('YES')
else:
    print('NO')