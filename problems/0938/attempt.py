n=int(input())
T=list(map(int, input().split()))
T.sort()
g=[0]*n
f=[i for i in range(1025)]
f[1]=0
s=[]
for i in range(2,len(f)):
    c=1
    if f[i]!=0:
        s.append(f[i])
    while 1:
        try:
            c+=1
            f[c*i]=0
        except:
            break
for i in range(n):
    for l in s:
        if T[i]%l==0:
            g[i]+=1
print(T[g.index(max(g))])