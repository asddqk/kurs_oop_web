n,m,k=map(int,input().split())
if k<=2:
    print(0)
else:
    a=n//(k-2)
    ao=n%(k-2)
    ai=a
    if ao!=0:
        ai=a+1
    b=m//2
    bo=m%2
    if ai>b:
        print(0)
    else:
        e=a
        b-=a
        e+=(b*2+ao+bo)//k
        if (b*2+ao+bo)%k!=0:
            e+=1
        print(e)