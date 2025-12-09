f1,g1,h1=map(int,input().split("."))
f2,g2,h2=map(int,input().split("."))
e=[31,28,31,30,31,30,31,31,30,31,30,31]

t=0
while 1:
    if h1==h2 and f1==f2 and g1==g2:
        break
    if f1==e[g1-1]:
        f1=0
        g1+=1
    if g1==13:
        h1+=1
        g1=1
    t+=1
    f1+=1
print(t)