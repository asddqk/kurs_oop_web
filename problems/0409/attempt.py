n=int(input())
T=list(map(int,input().split()))
s=0
for i in range(n-1):
    s+=abs(T[i]-T[i+1])/2+min(T[i],T[i+1])
print(s/(n-1))