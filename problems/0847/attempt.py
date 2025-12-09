n,m=input().split()
x=0
if sorted(n)==sorted(m):
    for i in range(len(n)):
        if n[i]==m[i]:
            x+=1
    if x>=1:
        print('NO')
    else:
        print('YES')
else:
    print('NO')