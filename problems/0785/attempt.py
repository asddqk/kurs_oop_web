n,m=map(int,input().split())
for i in range(n,m+1):
    if (i*i)%int('1'+'0'*len(str(i)))==i:
        print(i,end=' ')