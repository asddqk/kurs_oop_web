n=int(input())
T=list(map(int,input().split()))
f=list(set(T))
g=[0]*len(f)
for i in range(n):
    g[f.index(T[i])]+=1
q=sorted(g)
q=q[::-1]
if len(f)==1:
    print(T[0])
else:
    if q[0]==q[1]:
        print(0)
    else:
        print(f[g.index(max(g))])