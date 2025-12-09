n=int(input())
a=[0]*(10**6+5)
a[1]=1
for i in range(2,len(a)):
    h=[a[i-1]]
    if i%2==0:
        h.append(a[i//2])
    if i%3==0:
        h.append(a[i//3])
    a[i]=min(h)+1
print(a[n]-1)