n=int(input())
T=list(map(int,input().split()))
ep=[]
eo=[]
sp=0
so=0
for i in range(n):
    if T[i]>=0:
        sp+=T[i]
        ep.append(i+1)
    else:
        so+=abs(T[i])
        eo.append(i+1)  
if sp>so:
    print(len(ep))
    print(*ep)
else:
    print(len(eo))
    print(*eo)