j=int(input())
h2=2008
f2=1
g2=1
e=[31,29,31,30,31,30,31,31,30,31,30,31]
WE=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
t=0
while t!=j:   
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
    t+=1
    f2+=1
f2=str(f2)
g2=str(g2)
if len(f2)==1:
    f2='0'+f2
    
if len(g2)==1:
    g2='0'+g2
print(f'{WE[(j+1)%7]}, {f2}.{g2}')