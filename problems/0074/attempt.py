n, m = map(int, input().split())
if m==1:
    print(n)
else:
    e = 0
    while True:
        if m % 2 == 0:
            e += m // 2
            break
        e += n // 2
        n = n // 2 + n % 2
        m = m - m // 2
    print(e)