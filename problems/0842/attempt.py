n=int(input())
k='0,'
u=1
Key=0
while 1:
    if u<n:
        u*=10
        k+=str(u//n)
        u%=n
    if u==0 or len(k)>10000:
        if u==0:
            Key=0
        else:
            Key=10
        break
print('NO' if Key==0 else 'YES')