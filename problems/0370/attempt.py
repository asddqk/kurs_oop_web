n=int(input())
T=[list(map(int, input().split())) for i in range(n)]
T+=[T[0]]
print(abs(sum([T[i][0]*T[i+1][1]-T[i][1]*T[i+1][0] for i in range(n)]))/2)