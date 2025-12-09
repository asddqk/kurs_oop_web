n = int(input())
r=range
T = [list(map(int,input().split())) for i in r(n)]
E=[0]
for i in r(n):
    E.append(min([E[-i+k-1]+T[k][i-k] for k in r(i+1)]))
print(E[-1])