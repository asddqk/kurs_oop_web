n = int(input())


def F(n):
    s = sum([int(l) for l in str(n)])
    if n in [1, 4, 6, 8, 9]:
        return 0
    else:
        i = 2
        T = []
        while i <= n ** 0.5:
            if n % i == 0:
                T.append(i)
                n //= i
            else:
                i += 1
        if len(T) == 0:
            return n
        else:
            return F(s)


print(F(n))