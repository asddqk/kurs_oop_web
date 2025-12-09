n=int( input())
T=[list(map(int,input().split())) for i in range(n)]
for Round in range(n):
    E = [[0] * n for i in range(n)]
    for i in range(n):
        for l in range(n):
            E[i][l]=min(T[i][l],T[Round][l]+T[i][Round])
    T=E
for i in E:
    print(*i)