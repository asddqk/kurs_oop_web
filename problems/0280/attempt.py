n=int(input())
d={}
for i in range(2,1009):
    while n%i==0:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
        n//=i
        if n==0:
            break
    if n==0:
        break
t=list(d.values())
e=1
for i in t:
    e*=i
print(e)