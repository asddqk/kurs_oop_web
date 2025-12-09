n,m=map(int, input().split())
c=0
for i in range(n,m+1):
    f=1
    for l in str(i):
        f*=int(l)
        if f ==0:
            break
    if f!=0:
        if i%f==0:
            c+=1
print(c)