n=int(input())
T=[input() for i in range(n)]
opo=int(input())
R=[input() for i in range(opo)]
Print=[]
for i in range(n):
    F=0
    for l in range(opo):
        Ch=0
        if len(T[i])==len(R[l]):
            for y in range(len(T[i])):
                if Ch==2:
                    break
                else:
                    if T[i][y]!=R[l][y]:
                        Ch+=1
            if Ch==1:
                F+=1
    Print.append(F)
print(*Print)