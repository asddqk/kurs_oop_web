def f(x1, y1, x2, y2, x3, y3):
    if x2 - x1 != 0:
        z = ((y2 - y1) / (x2 - x1)) * x + y1 - ((y2 - y1) / (x2 - x1)) * x1
        if z <= max(y1, y2) and z >= min(y1, y2) and x >= min(x1, x2) and x <= max(x1, x2):
            T.append(z)
    if x3 - x2 != 0:
        z = ((y3 - y2) / (x3 - x2)) * x + y2 - ((y3 - y2) / (x3 - x2)) * x2
        if z <= max(y2, y3) and z >= min(y2, y3) and x >= min(x3, x2) and x <= max(x3, x2):
            T.append(z)
    if x1 - x3 != 0:
        z = ((y3 - y1) / (x3 - x1)) * x + y3 - ((y1 - y3) / (x1 - x3)) * x3
        if z <= max(y1, y3) and z >= min(y1, y3) and x >= min(x1, x3) and x <= max(x1, x3):
            T.append(z)

    if len(T) != 0 and y <= max(T) and y >= min(T):
        return 1
    return 0
e=0
for h in range(int(input())):
    x, y, x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    T = []
    if f(x1, y1, x2, y2, x3, y3)+f(x4, y4, x2, y2, x3, y3)+f(x1, y1, x4, y4, x3, y3)+f(x1, y1, x2, y2, x4, y4)>0 or [x, y] in [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]:
        e+=1
print(e)