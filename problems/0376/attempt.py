f1,g1=map(int,input().split())
f2,g2,h2=map(int,input().split())
e=[31,28,31,30,31,30,31,31,30,31,30,31]
t=0
if h2%400==0:
    e[1]=29
else:
    if h2%4==0 and h2%100!=0:
        e[1]=29
    else:
        e[1]=28 
while 1:   
    if g1==g2 and f1==f2:
        break
    if f2==e[g2-1]:
        f2=0
        g2+=1
    if g2==13:
        h2+=1
        g2=1
        if h2%400==0:
            e[1]=29
        else:
            if h2%4==0 and h2%100!=0:
                e[1]=29
            else:
                e[1]=28 
    if g1==g2 and f1==f2:
        break    
    t+=1
    f2+=1
print(t)