n,k=map(int,input().split())
if n==1:
    print('Yes')
else:
    T=[[0]*n for i in range(n)]
    Q=[]
    while 1:
        try:
            x,y=map(int,input().split())
            T[y-1][x-1]=1
            Q.append(x)
            Q.append(y)
        except:
            break
    Q=list(set(Q))
    c=0
    for i in T:
        if sum(i)==0:
            c+=1
    if n==len(Q) and c==1:
        if sum(T[k-1])==0:
            print('Yes')
        else:
            print('No')
    else:
        print('No')