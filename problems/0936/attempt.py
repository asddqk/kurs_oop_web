X,Y,R=map(float,input().split())
n=int(input())
T=[]
V=[]
for v in range(n):
    x,y=map(int,input().split())
    if ((x-X)**2+(y-Y)**2)**0.5<=R:
        T.append([x,y])
        if X!=x:
            k=(Y-y)/(X-x)
            b=Y-k*X
            V.append([k,b])
E=0
E1=0
for l in T:
    x, y = l
    if x<=X:
        E+=1
    if x>=X:
        E1+=1
Max=max(E1,E)
for i in V:
    E = 0
    E1=0
    for l in T:
        x,y=l
        if y<=i[0]*x+i[1]:
            E+=1
        if y>=i[0]*x+i[1]:
            E1+=1
    Max=max(E1,E,Max)
print(Max)