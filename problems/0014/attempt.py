a,b = map(int, input().split())
e=min(a,b)
r=0
t=e
while a*b + 1 > t:
    if t%a==0 and t%b==0:
        print(t)
        break
    t+=e