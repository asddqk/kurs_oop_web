n,m,k=map(int,input().split())
if k>=m:
    print(n*m)
else:
    z=m//k+(k-1)
    print(z*n)