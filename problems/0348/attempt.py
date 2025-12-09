x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())
x4,y4=map(int,input().split())

def F(x,y,X,Y):
    if x-X==0:
        return 'key', 'key'
    else:
        return (y-Y)/(x-X) , y -(y-Y)/(x-X)*x
    
k1,b1=F(x1,y1,x2,y2)
k2,b2=F(x3,y3,x4,y4)
if k1==k2 and b1!=b2:
    print('No')
else:
    if k1==k2:
        if (min(x1,x2)<=x3<=max(x1,x2) and min(y1,y2)<=y3<=max(y1,y2)) or (min(x1,x2)<=x4<=max(x1,x2) and min(y1,y2)<=y4<=max(y1,y2)) or (min(x3,x4)<=x1<=max(x3,x4) and min(y3,y4)<=y1<=max(y3,y4)) or (min(x3,x4)<=x2<=max(x3,x4) and min(y3,y4)<=y2<=max(y3,y4)):
            print('Yes')
        else:
            print('No')
    else:
        if 'key' in [k1,k2]:
            if 'key'==k1:
                pass
            else:
                k1,b1,k2,b2=k2,b2,k1,b1
                x1,y1,x2,y2,x3,y3,x4,y4=x3,y3,x4,y4,x1,y1,x2,y2
            if min(y1,y2)<=k2*x2+b2<=max(y1,y2) and min(y3,y4)<=k2*x2+b2<=max(y3,y4) and min(x3,x4)<=x2<=max(x3,x4):
                print('Yes')
            else:
                print('No')            
        else:
            X0=(b2-b1)/(k1-k2)
            Y0=k1*X0+b1
            if min(x1,x2)<=X0<=max(x1,x2) and min(x3,x4)<=X0<=max(x3,x4) and min(y1,y2)<=Y0<=max(y1,y2) and min(y3,y4)<=Y0<=max(y3,y4):
                print('Yes')
            else:
                print('No')