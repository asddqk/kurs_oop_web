x1,y1= map(int, input().split())
x2,y2= map(int, input().split())
t=int(input())
S=0
R=1
for i in range(t):
    X,Y= map(int, input().split())
    Gip1= pow(((X-x1)**2 + (Y-y1)**2),0.5)
    Gip2= pow(((X-x2)**2 + (Y-y2)**2),0.5)
    if Gip2 >= Gip1*2:
        S=1
        R+=i
        break
if S==1:
    print(R)
else:
    print('NO')