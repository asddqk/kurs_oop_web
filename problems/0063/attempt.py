p, q=map(int, input().split())
for i in range(1, p):
    x=i
    y=int(q/x)
    if x+y==p and x*y==q:
        print(min(x,y),max(x,y))
        break