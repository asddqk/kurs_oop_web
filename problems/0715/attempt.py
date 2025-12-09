H,S=map(int, input().split())

R=[]
c=0
for i in range(H+H+1):
    r2=list(input())
    R.append(r2)
T=R[:H]
t=R[H+1:]
for i in range(H):
    for l in range(S):
        if T[i][l]==t[i][l]:
            c+=1
        
print(c)