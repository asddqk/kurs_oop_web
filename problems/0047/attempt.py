n=int(input())
Max=1
c=1
def F(e):
    S=0
    for r in str(e):
        S+=int(r)
    return S
for i in range(1,n+1):
    if n%i==0:
        if F(i)>Max:
            Max=F(i)
            c=i
print(c)