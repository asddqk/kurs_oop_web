n,s=map(int,input().split())
T=list(map(int,input().split()))
T.sort()
c=0
for i in range(n):
    if s-T[i]>=0:
        c+=1
        s-=T[i]
print(c)