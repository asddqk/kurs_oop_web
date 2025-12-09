z, x = map(int, input().split())

if z < x:
    z, x = x, z
while x != 0:
    z, x = x, z % x
t, t1 = 0, 1
e = 0
f=10**9
while e != z:
    t, t1 = t1, (t1 + t)%f
    e += 1
print(t)