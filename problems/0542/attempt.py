n= int(input())
L=''
while n//2!=0:
    L+=str(n%2)
    n=n//2
L+=str(n%2)
U=''
for i in range(len(L)-1,-1,-1):
    U+=L[i]
_101=0
for i in range(len(U)):
    _101+=int(U[i])*(2**i)
print(_101)