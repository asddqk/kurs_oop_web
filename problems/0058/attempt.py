z=int(input())
for qwee in range(z):
    n,m=map(int, input().split())
    T=[]
    k1=0
    for i in range(n):
        T.append(list(map(int, input().split())))
    if n>1 and m>1:
        for i in range(n-1):
            for l in range(m-1):
                if (T[i][l]==0 and T[i][l+1]==0 and T[i+1][l]==0 and T[i+1][l+1]==0) or (T[i][l]==1 and T[i][l+1]==1 and T[i+1][l]==1 and T[i+1][l+1]==1):
                    k1=-1
                    break
        if k1==-1:
            print('NO')
        else:
            print('YES')  
    else:
        print('YES')