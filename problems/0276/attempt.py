n,m=map(int, input().split())
f=n%m
for i in range(m):
    if i>=(m-f):
        print(n//m+1,end =' ')
    else:
        print(n//m,end =' ')