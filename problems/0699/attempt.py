def g():
    return map(int,input().split())
k,t=g()
E=9**9
T=[list(g()) for i in [8]*k]
for i in T:
    for l in T:
        if i!=l:
            E=min(E, (( (l[0]-i[0])**2+(l[1]-i[1])**2)**0.5-l[2]-i[2])/2)
print(t if k==1 or t <E else E)