n=int(input())
T=[[0]*n for i in range(n)]
i=0
W=0
H=0
KEY=0
M=[H,W]
Password=0
while i!=n*n:
    i+=1
    T[H][W]=i
    if W==0 and H==0:
        W+=1
    else:
        if (W==0 and H==n-1 and n%2==0) or n%2==1 and W==n-1 and H==0:
            Password=-1
        if Password==0:
            if H==0 and W+1!=n and T[H][W-1]+1!=T[H][W]:
                W+=1
            elif W==0 and H+1!=n and T[H-1][W]+1!=T[H][W]:
                H+=1
            else:
                if H==0:
                    Key='Hight'
                else:
                    if W==0:
                        Key='Wight'
                if Key=='Hight':
                    H+=1
                    W-=1
                else:
                    W+=1
                    H-=1
        else:
            if H==n-1 and T[H][W-1]+1!=T[H][W]:
                W+=1
            elif W==n-1 and T[H-1][W]+1!=T[H][W]:
                H+=1
            else:
                if H==n-1:
                    Key='Hight'
                else:
                    if W==n-1:
                        Key='Wight'
                if Key=='Hight':
                    H-=1
                    W+=1
                else:
                    W-=1
                    H+=1            

#для тех кто смотрит решение. Здесь я отзеркалил список по диагонали>>>
U=[]
for i in range(n):
    X=[]
    for j in range(n):
        X.append(T[j][i])
    U.append(X)
    
for i in range(n):
    print(*U[i])