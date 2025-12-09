import math

x, y = map(float, input().split())
n, m, r = map(float, input().split())
b = max(((n - x) ** 2 + (m - y) ** 2 - r ** 2), 0) ** 0.5
print(r * r * math.pi * (1 - math.atan(b / r) / math.pi) + b * r)