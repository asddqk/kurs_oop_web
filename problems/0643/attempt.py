z=n=int(input())
s=1
while n!=1:
    if n%2==1:
        s+=1
    n//=2
print(s+z)