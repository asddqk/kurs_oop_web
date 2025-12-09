n,k=map(str,input().split())
n=int(n)
r=n%10+2
s=0
if r==11:
    c=['0','1','2','3','4','5','6','7','8','9','A','B']
    for i in range(len(str(k))):
        s+=c.index(k[len(k)-i-1])*(r**i)
else:
    k=int(k)
    for i in range(len(str(k))):
        s+=(k%10)*(r**i)
        k//=10    
print(s)