n,m=map(int,input().split())
T=[list(input()) for i in range(n)]
a,b=[],[]
for i in range(n):
    for l in range(m):
        if (i+l+int('W'==T[i][l]))%2==1:
            a.append([i+1,l+1])
        else:
            b.append([i+1,l+1])
print(min(len(a),len(b)))
for i in min(a,b,key=len):
    print(*i)