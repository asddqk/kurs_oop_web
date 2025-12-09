a,s,d=map(int,input().split())

if a+s==d or a+d==s or s+d==a:
    print('YES')
else:
    print('NO')