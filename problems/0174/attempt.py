N=int(input())
T=list(map(int, input().split()))
Z=float(input())
NACH=Z
T.sort()
for i in range(N):
    if T[i]>=Z:
        Z+=T[i]
        Z=Z/2
print("{0:.6f}".format(Z))