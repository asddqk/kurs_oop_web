n=int(input())
c=n
for i in range(2,37):
    f=[]
    n=c
    while n!=0:
        f.append(n%i)
        n//=i
    if len(f)==len(set(f)):
        print(i,end=' ')