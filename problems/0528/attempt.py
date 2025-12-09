n,i=map(int, input().split())
S=0
for k in range(1,i+1):
    S+=(n*k)-1-k*2
print(S+i*2+1)