a,b,c,d=map(int, input().split())
R=a-b-c-d
if R<0:
    R=abs(R)
    print(abs(R),max(a-c-d,0),max(a-b-d,0))
else:
    print(0,b,c)