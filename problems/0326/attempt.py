input()
R=[int(i) for i in input().split()]
o=10**6
T=[0]*(o*2+5)
for i in R:
    T[i+o]+=1
e=max(T)
x,c=T.index(e)-o,e
for i in R: 
    if i != x: print(i , end=' ')
print(*[x]*c)