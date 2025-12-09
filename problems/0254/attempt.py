n= int(input())
T=list(map(int, input().split()))
e=int(input())
Z=[]
for i in range(e):
    Z.append(list(map(int, input().split())))
for i in range(n):
    for l in range(e):
        if T[i]==Z[l][0]:
            T[i]=Z[l][1]
            break
print(*T)