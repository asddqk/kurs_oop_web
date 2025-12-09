n=int(input())
W=0
T=[]
for i in range(n):
    S=input()
    T.append(S)
    for k in S:
        if k=='C':
            W+=1
W//=2
C=0
R=[]
for k in range(n):
    E=[]
    for g in range(n):
        E.append(0)
    R.append(E)
for i in range(len(T)):
    if C==W:
        break    
    for l in range(len(T[i])):
        if T[i][l]=='D':
            R[i][l]=1
        if T[i][l]=='C':
            R[i][l]=1
            C+=1
        if C==W:
            break

for i in range(len(T)):   
    for l in range(len(T[i])):
        if R[i][l]==0:
            R[i][l]=2
for i in R:
    print(*i,sep='')