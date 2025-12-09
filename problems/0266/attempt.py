n = int(input())
if n == 0:
    print(0)
else:
    T = set([i for i in range(60 * 24)])
    for iii in range(n):
        a, b, c, d = map(int, input().split())
        time1 = a * 60 + b
        time2 = c * 60 + d
        ERI = []
        if time1 == time2:
            ERI = [i for i in range(60 * 24)]
        elif time1 < time2:
            ERI = [i for i in range(time1, time2)]
        else:
            ERI = [i for i in range(0, time2)]
            for k in range(time1, 24 * 60):
                ERI.append(k)
        T = T & set(ERI)
    print(len(T))