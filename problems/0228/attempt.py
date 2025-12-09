n=int(input())
def f():
    return map(float,input().split())
a,b=f()
e=100
for i in range(n-1):
    c, d =f()
    e*=max(c/a,d/b,1)
    a,b=c,d
print("{:.2f}".format(e))