s=int(input())
n=input().split()
pp=str()
oo=str()

for i in range(len(n)):
    n[i]=int(n[i])
    if n[i]%2==1:
        pp=pp + ' ' + str(n[i])
    else:
        oo=oo + ' ' + str(n[i])
print(pp)
print(oo)
if len(pp)>len(oo):
    print('NO')
else:
    print('YES')