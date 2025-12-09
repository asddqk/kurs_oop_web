k=int(input())
if 6%k==0:
    print(-1)
elif k//2==2:
    print(*['2101','12002'][k-4],sep='\n')
else:
    a=[0]*k
    a[0]=2
    a[1]=1
    a[k-5]=1
    a[k-1]=k - 4
    print(*a,sep='\n')