k,m,n = map(int, input().split())
if n<k:
    D=2
else:
    n*=2
    if n%k==0:
        D=n//k
    else:
        D=n//k + 1
print(D*m)