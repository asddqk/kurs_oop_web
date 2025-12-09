n = input()
if '0' in n:
    print('No')
else:
    n = sorted([int(i) for i in n])
    s = ''
    for i in range(len(n)):
        s += str(n[i])
    x = s[::-1]
    s = int(s)
    x = int(x)
    c = 0
    c1 = 0
    for i in range(2, int(s ** 0.5 + 2)):
        if s % i == 0:
            c += 1
            break
    for i in range(2, int(x ** 0.5 + 2)):
        if x % i == 0:
            c1 += 1
            break
    if c == 0 and c1 == 0:
        print('Yes')
    else:
        print('No')