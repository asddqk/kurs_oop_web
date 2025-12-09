X=int(input())
T=list(map(int, input().split()))
N=list(map(int, input().split()))
o=0
J=[]
for i in range(X):
    J.append(T[i]*(N[i]/100))
Mx=max(J)
for i in range(X):
    if T[i]*(N[i]/100)==Mx:
        print(i+1)
        break