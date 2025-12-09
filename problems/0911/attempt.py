n,m=map(str, input().split())
m=int(m)
c=m
i=0
s='2'
while c>3**i:
    c-=3**i
    i+=1
for i in range(i,0,-1):
    if 0<c<=3**i/3:
        s+='1'
    elif 3**i/3<c<=3**i/3*2:
        s+='0'
    else:
        s+='2'
    c%=3**(i-1)
f1=[m]
f2=[]
for i in range(len(s)):
    if s[i]=='1':
        f1.append(3**(len(s)-i-1))
    if s[i]=='2':
        f2.append(3**(len(s)-i-1))
f1.sort()
f2.sort()
f1.pop(f1.index(m))
if n=='R':
    f1,f2=f2,f1
print('L:', end='')
print(*f1)
print('R:', end='')
print(*f2)