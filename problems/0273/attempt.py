s = input()
R = []
c = 0
l = s[0]
if len(s) > 2:
    for i in range(len(s)):
        if s[i] == l:
            c += 1
        else:
            R.append([l, min(c, 3)])
            c = 1
            l = s[i]
    R.append([l, min(c, 3)])
    d = 0
    for i in range(100, 1000):
        h = i
        T = []
        i = list(str(i))
        for jkl in range(len(R)):
            X = []
            for lkj in R[jkl]:
                X.append(lkj)
            T.append(X)
        l = 0
        while len(i) > 0:
            if T[l][0] == i[0]:
                i.pop(0)
                T[l][1] -= 1
            else:
                l += 1
            if l >= len(T):
                break
            if T[l][1] == 0:
                l += 1
            if l >= len(T):
                break
        if len(i) == 0:
            d += 1
    print(d)
else:
    print(0)