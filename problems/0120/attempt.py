n,m=map(int, input().split())
c=range
T=[list(map(int,input().split())) for i in c(n)]
for i in c(1,n):
    T[i][0]+=T[i-1][0]
for i in c(1,m):
    T[0][i]+=T[0][i-1]
for i in c(1,n):
    for l in c(1, m):
        T[i][l]= min(T[i][l-1]+T[i][l],T[i-1][l]+T[i][l])
print(T[n-1][m-1])