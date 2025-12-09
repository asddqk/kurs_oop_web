n=int(input())
T=[[0,0]]
for i in range(n):
    T.append(list(map(int,input().split())))
s=0
for i in range(n+1):
    x,y=T[i-1][0],T[i-1][1]
    xx,yy=T[i][0],T[i][1]
    s+=((x-xx)**2+(y-yy)**2)**0.5
print(s)