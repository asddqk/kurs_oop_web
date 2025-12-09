n=int(input())
T=[[0]*n for i in range(n)]
i=0
W=0
H=0
M=[-1,n]
KEY=0
while i!=n*n:
    i+=1
    T[H][W]=i
    if H==1+KEY and W==0+KEY:
        M=[0+KEY,n-1-KEY]
        KEY+=1
    if H==0 and W==0:
        W+=1
    else:
        if W+1==M[1]:
            if H+1==M[1]:
                W-=1
            else:
                H+=1
        else:
            if H-1>M[0]:
                if W-1>M[0]:
                    W-=1
                else:
                    H-=1
            else:
                W+=1
    
for y in T:
    print(*y)