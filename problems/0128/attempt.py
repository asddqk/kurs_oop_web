n=int(input())
x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
T=[[0]*(n+1) for i in range(n+1)]
T[y1][x1]=1
while T[y2][x2]==0:
    T1=[i.copy() for i in T]
    for x in range(1,n+1):
        for y in range(1,n+1):
            if T[y][x]>0:
                for Y in range(y-2,y+3):
                    for X in range(x-2,x+3):
                        if 1<=Y<=n and 1<=X<=n and abs(X-x)+abs(Y-y)==3:
                            if T[Y][X]==0:
                                T1[Y][X]=T[y][x]+1
                            else:
                                T1[Y][X]=min(T[y][x]+1,T[Y][X])
    T=T1
print(T[y2][x2]-1)