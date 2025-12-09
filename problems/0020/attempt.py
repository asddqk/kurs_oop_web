n = int(input())
k = list(map(int, input().split()))
s=0
m=0
for i in range(n-1):
    a,b=k[i],k[i+1]
    if a>b:
        if k[i-1]>k[i]:
            s = 0
        s+=1
    elif a<b:
        if k[i-1]<k[i]:
            s = 0
        s += 1
    else:
        s=0
    m=max(m,s)
print(m+1)