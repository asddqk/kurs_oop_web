n,m,k=map(int, input().split())
S=''
n=n%m
for i in range(k+100):
    n*=10
    S+=str(n//m)
    n=n%m
print(S[k-1])