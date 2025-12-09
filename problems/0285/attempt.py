n,k=map(int,input().split())
T=list(map(int,input().split()))
S=[]
for i in T:
    if i<=k:
        S.append(i)
if k<=(sum(S)-n+1):      
    print('yes')
else:
    print('no')