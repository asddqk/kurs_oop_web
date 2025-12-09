n=int(input())
T=list(map(int,input().split()))
r=int(input())
e=0
for i in T:
    if i<=r:
        e+=i
    else:
        e+=r
print(e)