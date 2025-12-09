Z=int(input())
sch=0
for i in range(Z):
    T,t=map(str, input().split('->'))
    if T[0]==t[0]:
        sch+=1
print(sch)