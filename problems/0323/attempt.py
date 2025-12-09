n= int(input())
T=[]
u=0
for i in range(2,1001):
    for l in range(2,i):
        if i%l==0:
            u+=1
    if u==0:
        T.append(i)
    u=0
    
for i in range(len(T)):
    if u==1:
        break
    for j in range(len(T)):
        if T[i]+T[j]==n:
            print(min(T[i],T[j]), max(T[i],T[j]))
            u+=1