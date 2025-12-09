n=int(input())
if n==0 or n==1:
    print(10 if n==0 else 1)
else:
    S=[]
    while n!=1:
        c=n
        for i in range(9,1,-1):
            if n%i==0:
                S.append(i)
                n//=i
                break
        if c==n:
            break
    if n!=1:
        print(-1)
    else:
        S.sort()
        E=''
        for i in S:
            E+=str(i)
        print(E)