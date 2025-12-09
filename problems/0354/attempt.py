n = int(input())
i = 2
while i <= n ** 0.5:
    if n % i == 0:
        print(i, end='')
        n //= i
        if n > 1:
            print('*', end='')
    else:
        i += 1
if n > 1:
    print(n)