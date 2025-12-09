n,m=sorted(map(int,input().split()))
if n==1:
    print(m*4)
else:

    if n%2==0 and m%2==0:
        S = 2 * m * n + 2*n + 2*m
    else:
        S = 2 * m * n + n + m
        S+=n+m-2
        if n*m%2==0:
            S+=2
    print(S)