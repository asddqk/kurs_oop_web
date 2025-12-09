n,m = map(int, input().split())
n=str(n)
m=str(m)
_101=0
for i in range(len(n)):
    _101+=int(n[i])*(3**(len(n)-(i+1)))
for i in range(len(m)):
    _101+=int(m[i])*(3**(len(m)-(i+1)))
print(_101)