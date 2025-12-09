n = int(input())
a, b, c = n // 144, 0, 0
SUM = 10 ** 90
j = 0
while j < 1000:
    j += 1
    if a * 1140 + b * 102.5 + c * 10.5 < SUM and a * 144 + b * 12 + c >= n:
        T = [a, b, c]
        SUM = a * 1140 + b * 102.5 + c * 10.5
    c += 1
    if c > 12:
        c = 0
        b += 1
    if b > 12:
        b = 0
        a += 1
print(*T)