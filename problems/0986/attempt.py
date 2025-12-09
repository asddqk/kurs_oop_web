n,bx,by,l=map(int,input().split())
f=0
for hgi in range(n):
    x,y=map(int,input().split())
    h=((bx-x)**2+(by-y)**2)**0.5
    if h>l:
        f+=1
    else:
        break
if n==f:
    print('Yes')
else:
    print(f+1)