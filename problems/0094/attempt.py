n,m,k=map(int, input().split())
i=0
if k>=n and m>n:
    print('NO')
else:
    while m>0:
        i+=1
        m-=n
        if m<=0:
            break
        m+=k
    print(i)