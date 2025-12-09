n,m=map(int, input().split())
if max(n,m)%2==1:
    print(max(n,m)//2+1,min(n,m))
else:
    print(max(n,m)//2,min(n,m))