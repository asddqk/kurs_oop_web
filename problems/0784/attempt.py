int(input())
s=int(input())
f=int(input())
z=min(f,s)
v=max(f,s)
for i in range(0,66):
    if z>=2**i and z<2**(i+1):
        c=i
        break
for i in range(0,66):
    if v>=2**i and v<2**(i+1):
        break
for l in range(max(c,i)-min(c,i)):
    if v%2==1:
        v-=1
    v//=2    
s,f=v,z
while s!=f:
    if s%2==1:
        s-=1
    s//=2
    if f%2==1:
        f-=1
    f//=2  
print(f)