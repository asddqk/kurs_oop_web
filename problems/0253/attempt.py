n,k=map(int, input().split())
e,f=map(int, input().split())
t=0
while 1:
    if k==f and n==e:
        break
    if k==30:
        t+=1
    if k==60:
        k=0
        n+=1
        if n==12 or n==24:
            t+=12
        else:
            t+=(n%12)
    if n==24:
        n=0
    k+=1
    
print(t)