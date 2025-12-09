a = [sorted(map(int, input().split())) for i in [1] * 6]
a.sort()
x = 'POSSIBLE'
print(x if all([a[0][0] == a[3][0], a[0][1] == a[5][0], a[2][1] == a[5][1], a[0] == a[1], a[2] == a[3],
                a[4] == a[5]]) else 'IM' + x)