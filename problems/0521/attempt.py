n,k=map(int, input().split())
t=0
for i in range(n,k+1):
    while i!=2:
        if i%2==0:
            i//=2
        else:
            i*=3
            i+=1
        t+=1
print(t)