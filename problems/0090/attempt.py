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
x,y=F()
SD=[]
for tyut in range(int(input())):
    x1,y1,x2,y2,x3,y3=F()
    T=[]  
    E(x1,x2,y1,y2)
    E(x2,x3,y2,y3)
    E(x3,x1,y3,y1)
    if T!=[] and y<j(T) and y>q(T):
        SD.append(tyut+1)
print(len(SD))
print(*SD)