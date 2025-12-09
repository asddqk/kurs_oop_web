for i in range(int(input())):
    x,y=map(str,input().split())
    x=list(x)
    y=list(y)
    if set(x)==set(y):
        print('YES')
    else:
        print('NO')