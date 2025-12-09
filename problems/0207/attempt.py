s=int(input())
x,y=0,0
h=((2)**0.5)/2
for i in range(s):
    n,m=map(int, input().split())
    if n==1:
        y+=m
    if n==3:
        x+=m
    if n==5:
        y-=m
    if n==7:
        x-=m     

    if n==2:
        y+=m*h
        x+=m*h
    if n==4:
        x+=m*h
        y-=m*h
    if n==6:
        y-=m*h
        x-=m*h
    if n==8:
        x-=m*h
        y+=m*h
print(x,y)