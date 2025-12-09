n,m,k=map(int, input().split())
F=[k,m]
for i in range(33):
    F.append(F[i]-F[i+1])
print(F[n],F[n-1])