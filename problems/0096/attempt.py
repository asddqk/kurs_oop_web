n,m=map(int, input().split())
X,Y=map(int, input().split())
T=[[0]*m for i in range(n)]
W=0
H=0
Key='6'
while 1:
    if W>=m-1 or H==X-1 and W==Y-1:
        if H==X-1 and W==Y-1:
            T[H][W]=1
        break
    T[H][W]=1
    W+=1
while 1:
    if H>=n-1 or (H==X-1 and W==Y-1):
        if H==X-1 and W==Y-1:
            T[H][W]=1        
        break
    T[H][W]=1
    H+=1
while 1:
    if W<=-1 or (H==X-1 and W==Y-1):
        if H==X-1 and W==Y-1:
            T[H][W]=1        
        break
    T[H][W]=1
    W-=1 
if W<0:
    W=0

while 1:
    if (H==X-1 and W==Y-1):
        break    
    while 1:
        if T[H-1][W]==1 or (H==X-1 and W==Y-1):
            if H==X-1 and W==Y-1:
                T[H][W]=1            
            break
        T[H][W]=1
        H-=1
        
    while 1:
        if T[H][W+1]==1 or (H==X-1 and W==Y-1):
            if H==X-1 and W==Y-1:
                T[H][W]=1            
            break
        T[H][W]=1
        W+=1    
    while 1:
        if T[H+1][W]==1 or (H==X-1 and W==Y-1):
            if H==X-1 and W==Y-1:
                T[H][W]=1            
            break
        T[H][W]=1
        H+=1       
        
    while 1:
        if T[H][W-1]==1 or (H==X-1 and W==Y-1):
            if H==X-1 and W==Y-1:
                T[H][W]=1            
            break
        T[H][W]=1
        W-=1  
S=0
for y in T:
    S+=sum(y)
print(S)