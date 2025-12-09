l,n=map(int,input().split())
T=sorted(list(map(int,input().split())))
E=0
while len(T)>0:
    a=T[0]
    b=a+l*2
    E+=1
    while T[0]<=b:
        T.pop(0)
        if len(T)==0:
            break
print(E)