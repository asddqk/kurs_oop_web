z,x=map(int, input().split())

def F(z,x):
    if z<x:
        z,x=x,z
        
    while x!=0:
        z,x=x,z%x
    return z
print(F(z,x))