r,x,y=map(int,input().split())
x=abs(x)
if x==0:
    print(0)
else:
    print(r/((r+r-y)/x))