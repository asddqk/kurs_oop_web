n=int(input())
T=[list(map(int,input().split())) for i in range(n*n)]
R=[]
S=0
Key=[i for i in range(1,n*n+1)]
for j in range(n):
    for l in range(0,n*n,n):
        for i in range(j*n,j*n+n):
            R.extend(T[i][l:l+n])
        if sorted(R)==Key:
            S+=1
        R=[]
for i in range(n*n):
    if sorted(T[i])==Key:
        S+=1
for i in range(n*n):
    R=[]
    for l in range(n*n):
        R.append(T[l][i])
    if sorted(R)==Key:
        S+=1   
    
if S==n*n*3:
    print('Correct')
else:
    print('Incorrect')