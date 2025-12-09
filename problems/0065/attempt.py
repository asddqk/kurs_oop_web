s = input()
n = int(input())
T = []
try:
    for i in range(n):
        x = input()
        c = 0
        for l in range(len(s)):
            if x[l] == s[l]:
                c += 1
        T.append(len(s) - c)
    R = []
    Min = min(T)
    for i in range(len(T)):
        if T[i] == Min:
            R.append(i + 1)
    print(len(R))
    print(*R)
except:
    print(0)