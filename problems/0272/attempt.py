E=list(map(int, input().split()))
t1=[]
t2=[]

for i in range(len(E)):
    if i%2==0:
        t1.append(E[i])
    else:
        t2.append(E[i])
print(min(t1)+max(t2))