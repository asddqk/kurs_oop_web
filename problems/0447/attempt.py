n=int(input())
S=1
for i in range(1,n+1):
    S*=i
    while S%10==0:
        S//=10
print(S%10)