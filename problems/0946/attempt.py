T=[]
V=[]
for uuuu in range(int(input())):
    s=input()
    if ' ' in s:
        x,y=map(int,s.split())
        if x==1:
            E=[]
            E.append(y)
            E.extend(T)
            T=list(E)
        else:
            T.append(y)
    else:
        x=int(s)
        if x==3:
            V.append(T[0])
            T.pop(0)
        else:
            V.append(T[len(T)-1])
            T.pop(len(T)-1)            
print(*V)