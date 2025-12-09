n,m=map(int, input().split())
T=[i+1 for i in range(n)]
c=-1+m
if m==1:
    print(max(T))
else:
    while len(T)!=1:
        try:
            T[c]=0
            c+=m
        except:
            c-=len(T)
            E=[]
            for i in T:
                if i!=0:
                    E.append(i)
            T=E
    print(sum(T))