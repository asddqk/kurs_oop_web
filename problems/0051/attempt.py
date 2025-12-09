n,m=map(str,input().split())
S=n=int(n)
k=len(m)
i=1
while n-i*k>0:
    S*=(n-i*k)
    i+=1
print(S)