n = int(input())
L=[]
q=n
T=[]
for m in range(2,37):
    n=q
    while n//m!=0:
        L.append(str(n%m))
        n=n//m
    L.append(str(n%m))
    if L==L[::-1]:
        T.append(m)
    L=[]

if len(T)==0:
    print('none')
else:
    if len(T)==1:
        print('unique')
        print(*T)
    else:
        print('multiple')
        print(*T)