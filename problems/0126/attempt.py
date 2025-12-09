q=range
n=int(input())
T=[list(map(int,input().split())) for i in q(n)]
M=9**9
for i in q(n):
    for l in q(i+1,n):
        for j in q(l+1,n):
            M=min(M,T[i][l]+T[l][j]+T[j][i])
print(M)