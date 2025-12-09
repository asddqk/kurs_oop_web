n=int(input())
E=0
R=bin(n)[2:]
for i in range(len(R)):
    if R[i]=='1':
        E+=1
print(E)