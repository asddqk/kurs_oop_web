n, m = map(int, input().split())
c = 0
for i in range(2 ** n):
    if bin(i)[2:].count('1') >= m:
        c += 1
print(c)