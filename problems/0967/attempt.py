n,m,k=map(int,input().split())
T=list(map(int,input().split()))
def s(x,k1):
    s=0
    while x!=0:
        s+=x%k1
        x//=k1
    return s
e=[]
for i in T:
    e.append(s(i,m)*s(i,k))
print(*sorted(e))