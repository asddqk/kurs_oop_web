n=int(input())
r,g,h,j=map(int, input().split())
if n==1:
    qq=(g+h+j)-(2*r)
    if qq<0:
        qq=0
    print(qq)
if n==2:
    print(min(g,h,j))