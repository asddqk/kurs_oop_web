a, b = map(str, input().split(' '))
s={'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8'}
for i in s:
    a = a.replace(i, s[i])
    b = b.replace(i, s[i])
x1, y1 = [int(i) for i in a]
x2, y2 = [int(i) for i in b]

def f(X1,Y1,X2,Y2):
    if X1>8 or X1<1 or Y1>8 or Y1<1:
        return 0
    if [X1,Y1]==[X2,Y2]:
        return 1
    return f(X1+1,Y1+1,X2,Y2)+f(X1-1,Y1+1,X2,Y2)
s=f(x1,y1,x2,y2)
if s==0:
    print('NO')
else:
    print('YES')