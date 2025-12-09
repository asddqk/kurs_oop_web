x1,y1,x2,y2=map(int, input().split())
A,B=map(int, input().split())
if x1==x2:
    if x1<=0 and A<=0:
        R=abs(max(abs(A),abs(x1))-min(abs(A),abs(x1)))
        if A<x1:
            print(x1+R,B)
        else:
            print(x1-R,B)
            
    elif x1>=0 and A>=0:
        R=abs(max(abs(A),abs(x1))-min(abs(A),abs(x1)))
        if A<x1:
            print(x1+R,B)
        else:
            print(x1-R,B)   
            
    elif x1>=0 and A<=0:
        R=x1-A
        print(x1+R,B)
            
    elif x1<=0 and A>=0:
        R=A-x1
        print(x1-R,B)
    else:
        print(A,B)
elif y1==y2:
    if B<=0 and y1<=0:
        R=abs(max(abs(B),abs(y1))-min(abs(B),abs(y1)))
        if y1<B:
            print(A,y1-R)
        else:
            print(A,y1+R)
    elif B>=0 and y1>=0:
        R=abs(max(abs(B),abs(y1))-min(abs(B),abs(y1)))
        if y1<B:
            print(A,y1-R)
        else:
            print(A,y1+R)        
    elif B<=0 and y1>=0:
        R=y1-B
        print(A,y1+R) 
    elif B>=0 and y1<=0:
        R=B-y1
        print(A,y1-R)     
    else:
        print(A,B)