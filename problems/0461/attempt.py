xcv=int(input())
T=list(map(int,input().split()))
T.sort()
Max=0
for i in range(xcv//2+1):
    Max+=(T[i])//2+1
print(Max)