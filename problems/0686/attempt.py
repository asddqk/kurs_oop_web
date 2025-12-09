n=int(input())
e=[0]*n
T=sorted(list(map(int,input().split())))
Key=0
g=0
l=0
for i in T:
    if Key==0:
        e[g]=i
        Key=1
    else:
        Key=0
        g+=1
        e[n-g]=i
print(*e)