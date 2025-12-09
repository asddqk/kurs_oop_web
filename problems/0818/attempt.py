N=int(input())
j=0
T=list(map(int, input().split()))
for i in range(N):
    j+=T[i]
print(j-(N-1))