N=int(input())
T=[]
for i in range(N):
    T.append(list(map(int, input().split())))
T=sorted(T)
for i in range(N):
    print(*T[i])