n = int(input())
Max = 0
i = 1
F = 0
while n - F > 0:
    if (n - F) % i == 0:
        Max = max(i, Max)
    F += i
    i += 1
print(Max)