x1, y1, x2, y2, x3, y3 = map(int, input().split())
a1=((x1-x2)**2+(y1-y2)**2)**0.5
a2=((x3-x2)**2+(y3-y2)**2)**0.5
a3=((x1-x3)**2+(y1-y3)**2)**0.5
if a1==max(a1,a2,a3):
    print(x1+x2-x3,y1+y2-y3)
elif a2==max(a1,a2,a3):
    print(-x1+x2+x3,-y1+y2+y3)
else:
    print(x1 - x2 + x3, y1 - y2 + y3)