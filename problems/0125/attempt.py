n=int(input())
T=[]
S=0
for i in range(n):
    T.append(list(map(int,input().split())))
input()
E=list(map(int,input().split()))
for i in range(n):
    for l in range(n):
        if T[i][l]==1:
            if E[i]!=E[l]:
                S+=1
print(S//2)