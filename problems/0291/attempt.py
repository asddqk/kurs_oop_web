n=int(input())
T=[input() for i in range(n)]
S=input()
c=0
for i in T:
    p=list(S)
    vv=len(i)
    for l in i:
        if l in p:
            p.pop(p.index(l))
            vv-=1
    if vv==0:
        c+=1
print(c)