f,t=map(int,input().split())
f1,t1=map(int,input().split())
f2,t2=map(int,input().split())
f3,t3=map(int,input().split())
if f+f1+f2+f3 > t+t1+t2+t3:
    print('1')
elif f+f1+f2+f3 < t+t1+t2+t3:
    print('2')
else:
    print('DRAW')