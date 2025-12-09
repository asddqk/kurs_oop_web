def F():
    return map(int, input().split())
q=min
j=max
def E(a,b,c,d):
    if b-a!=0:
        v=(d-c)/(b-a)
        z=v*x+c-v*a
        if z<=j(c,d) and z>=q(c,d) and x>=q(a,b) and x<=j(a,b):
            T.append(z)    
x1,y1=F()
x2,y2=F()
x3,y3=F()
x,y=F()
T=[]  
E(x1,x2,y1,y2)
E(x2,x3,y2,y3)
E(x3,x1,y3,y1)
print('In' if T!=[] and y<=j(T) and y>=q(T) else 'Out')