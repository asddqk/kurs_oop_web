n=input()
T=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
k=[0]*26
f=[]
d=list(n)
d.sort()
for i in d:
    f.append(T.index(i)+1)
c=0
for i in range(26):
    if f[i]>i:
        c+=1
if c==26:
    print('YES')
    c=0
    d=list(n)
    for i in T:
        for l in range(len(n)):
            if d[l]==i:
                k[c]=l+1
                c+=1
                
    print(*k)
else:
    print('NO')