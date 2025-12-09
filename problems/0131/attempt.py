n=int(input())
max=0
T=0
R=1
for i in range (n):
    
    v,s=map(int,input().split())
    if s==1 and v>max:
      max=v
      T=R
    R+=1
    
if T==0:
    print(-1)
else:
    print(int(T))