n,m = map(int, input().split())
L=''
while n//m!=0:
    L+=str(n%m)
    n=n//m
L+=str(n%m)
_1=1
_2=0
for i in range(len(L)):
    _1*=int(L[i])
    _2+=int(L[i])
print(_1-_2)