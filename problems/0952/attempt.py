n,m=map(int,input().split())
if n==m and n==0:
    print(0,0)
else:
    if n==0:
        print('Impossible')
    else:
        if m==0:
            print(n,n)
        else:
            if n>=m:
                e=n
            else:
                e=n+(m-n)
            b=n+m-1
            print(e,b)