s=input()
T=[]
L=len(s)
E=[]
Q=[0]*L
for i in s:
    if i not in T:
        T.append(i)
    else:
        d=0
        for l in range(len(E)):
            if E[l]==i:
                Q[l]+=1
                d=1
        if d==0:
            E.append(i)
            Q[len(E)-1]+=1
W=1
for i in range(L):
    W*=i+1
for l in range(len(Q)):
    d=1
    for i in range(1,Q[l]+1):
        d*=i+1
    W//=d
print(W)