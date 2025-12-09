n=int(input())
T=list(map(int, input().split()))
K="1"
e1=0
e2=0
while len(T)!=0:
    n-=1
    if K=="1":
        K="2"
        if T[n]>T[0]:
            e1+=T[n]
            T.pop(n)
        else:
            e1+=T[0]
            T.pop(0)
    else:
        K="1"
        if T[n]>T[0]:
            e2+=T[n]
            T.pop(n)
        else:
            e2+=T[0]
            T.pop(0)        
print(f"{e1}:{e2}")