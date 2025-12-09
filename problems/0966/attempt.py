[[10, 1], [1, 22], [6, 123], [12, 1124], [40, 11125], [30, 111126], [84, 1111127], [224, 11111128]]
n=int(input())
T=[]
for i in range(n):
    T.append(list(map(int, input().split())))
t=int(input())
V=0
for t in range(t):
    l=0
    while l<len(T):
        if t>=T[l][0] and t<T[l][1]:
            V+=T[l][2]
        if T[l][1]<t:
            T.pop(l)
        else:
            l+=1
    if V<0:
        V=0
print(V)