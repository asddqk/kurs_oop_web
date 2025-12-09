n,s=map(int,input().split())
T=[list(map(int,input().split())) for i in range(n)]
E=[s-1]
S=0
c=0
while c!=len(E):
    c=len(E)
    for i in E:
        for l in range(len(T[i])):
            if T[i][l]==1 and l not in E:
                E.append(l)
E=list(set(E))
if len(E)!=0:
    E.pop(E.index(s-1))
print(len(E))