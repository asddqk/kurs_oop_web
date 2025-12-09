n=int(input())
S=list(map(int,input().split()))
z1=0
for i in range(n-1):
    if S[i]>S[i+1] or S[i]+1!=S[i+1]:
        z1+=1
print(z1)