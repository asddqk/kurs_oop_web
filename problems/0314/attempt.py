n,m=map(int, input().split())
T=[]
for i in range(1,n+1):
    T.append(str(i))
T.sort()
for i in range(len(T)):
    if T[i]==str(m):
        print(i+1)
        break