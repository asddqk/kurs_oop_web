n= int(input())
for i in range(14):
    if n == 2**i:
        print('YES')
        break
else:
    print('NO')