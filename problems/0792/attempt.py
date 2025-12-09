n,p=map(int, input().split())
nn,pp=map(int, input().split())
v=0
vv=0
while n!=0:
    v+=(n%p)
    n//=p
while nn!=0:
    vv+=(nn%pp)
    nn//=pp

if v==vv:
    print(v)
else:
    print(0)