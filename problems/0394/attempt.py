def F(a,b):
    if b == 0:
        return a
    return F(b, a%b)
a, b = map(int, input().split())
print(a*b//F(a,b)//b)