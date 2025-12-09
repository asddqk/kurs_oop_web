a1,b1,c1=map(int,input().split())
a2,b2,c2=map(int,input().split())
a3,b3,c3=map(int,input().split())
def X(a,b,c,A,B,C):
    return (B*c-b*C)/(B*a-b*A),(c-a*((B*c-b*C)/(B*a-b*A)))/b

def Len(x,y,X,Y):
    return ((X-x)**2+(Y-y)**2)**0.5
x1,y1=X(a1,b1,c1,a2,b2,c2)
x2,y2=X(a3,b3,c3,a2,b2,c2)
x3,y3=X(a1,b1,c1,a3,b3,c3)
l1=Len(x1,y1,x2,y2)
l2=Len(x3,y3,x2,y2)
l3=Len(x1,y1,x3,y3)
p=(l1+l2+l3)/2
print((p*(p-l1)*(p-l2)*(p-l3))**0.5)