x, y = map(int, input().split())
d = 10 ** 9
if abs(x)==d or abs(y)==d:
    print('NO')
else:
    print('YES')
    print(x-1,y)
    print(x,y+1)
    print(x+1,y-1)