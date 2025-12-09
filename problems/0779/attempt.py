n=int(input())
T=list(map(int,input().split()))
S=sum(T[i]-T[0] for i in range(n))
dmax=0
for d in range(1,n):
    e=S+d*(T[d]-T[d-1])-(n-d)*(T[d]-T[d-1])
    if e<=S:
        dmax=T[d]
        S=e
print(dmax)