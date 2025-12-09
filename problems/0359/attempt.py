n = int(input())
z=1
if n < 2:
    print(n)
else:
    j = 0
    for i in range(1, n):
        if i % 2 == 0:
            j += 2
        z +=j + 1
    a = z // 10
    while (z+a)//10!=a:
        b=z+a
        a+=b//10-a
    z+=a
    if z % 10 == 0:
        z += 1
    print(z)