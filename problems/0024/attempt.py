n, m = map(int, input().split())
if m ==1:
    print(n)
elif m==0:
    print(1)
else:
    r=m-1
    s=0
    while m<=n:
        s+=n-m+1
        m+=r
    print(s)