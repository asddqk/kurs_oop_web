n, m = map(int, input().split())
TN = []
TM = []
i = 2
while i <= n ** 0.5:
    if n % i == 0:
        TN.append(i)
        n //= i
        if n == 1:
            break
    else:
        i += 1
if n != 1:
    TN.append(n)
i = 2
while i <= m ** 0.5:
    if m % i == 0:
        TM.append(i)
        m //= i
        if m == 1:
            break
    else:
        i += 1

if m != 1:
    TM.append(m)
i = 0
while i < len(TN):
    if TN[i] in TM:
        TM.pop(TM.index(TN[i]))
        TN.pop(i)
    else:
        i += 1
print(len(TN) + len(TM))