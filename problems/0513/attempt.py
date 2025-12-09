n=int(input())
N=1

KK=0
S=0

for i in range(1,n+1):
    N*=i
    
for k in range(2,n+1):
    n_k=1
    K=1
    
    for i in range(1,k+1):
        K*=i  
    R=n-k
    for i in range(1,R+1):
        n_k*=i
    
    S+=N/(K*n_k)
print(int(S))