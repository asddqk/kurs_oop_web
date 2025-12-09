s=input()
x,y=0,0
T=[[0,0]]
g=['up','right','down','left','up','right','down','left']
Key='up'
u=0
v=0
for i in s:
    if i=='L':
        Key=g[g.index(Key)-1]
    elif i=='R':
        Key=g[g.index(Key)+1]
    else:
        u+=1
        if Key=='up':
            y+=1
        if Key=='right':
            x+=1
        if Key=='down':
            y-=1
        if Key=='left':
            x-=1
        z=[x,y]
        if z in T:
            v=1
            break
        else:
            T.append(z)
if u==0 or v==0:
    print(-1)
else:
    print(u)