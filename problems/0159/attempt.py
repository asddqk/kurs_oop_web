n=int(input())
T=list(map(int,input().split()))
e=[0]*n
for i in range(n):
    e[T[i]-1]=i+1
print(*e)