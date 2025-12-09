n,m=map(int, input().split())
T=[]
for i in range(331):
    T.append(2**i)
g=0
for i in range(len(T)):
    if T[i]>n:
        if T[i]<n+m:
            g+=1
            v=T[i]
            break
            
if g==1:
    print(v)
else:
    print('NO')