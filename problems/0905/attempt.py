q=len
d=print
g=range
f=input
T=[]
E=[]
Key=[chr(i) for i in g(97,123)]
c='the quick brown fox jumps over the lazy dog'
for i in g(int(f())):
    x=f()
    T.append(x)
    if q(x)==q(c):
        if q(x.split())==q(c.split()) and q(set(x.replace(' ','')))==26:
            x=x.replace(' ','')
            c=c.replace(' ','')
            for i in g(q(c)):
                E.append([x[i],c[i]])
Q=[]
for i in g(q(E)):
    if E[i] not in Q:
        Q.append(E[i])
if q(Q)==26:
    for i in T:
        for l in i:
            if l==' ':
                d('',end=' ')
            else:
                for u in g(q(Q)):
                    if Q[u][0]==l:
                        d(Q[u][1],end='')
        d()
else:
    d('No solution')