m=int(input())
e=list(map(int, input().split()))
cvb=25000
T=[i for i in range(cvb)]
T[1]=0
k=''
for i in range(len(T)):
    if T[i]!=0:
        x=2
        while i*x<cvb:
            T[i*x]=0
            x+=1
    if T[i]!=0:
        k+=str(T[i])
for i in e:
    print(k[i-1],end='')