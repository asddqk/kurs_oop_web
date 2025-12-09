X=int(input())
T=list(map(int, input().split()))
n=len(T)
m=min(T)
T*=2
W=T
for i in range(n):
    if T[i]==m:
        if W>=T[i:i+n]:
            W=T[i:i+n]    
print(*W)