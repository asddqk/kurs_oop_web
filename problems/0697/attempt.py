L,W,H=map(int, input().split())

e=L*H*2 + W*H*2

if e%16==0:
    print(e//16)
else:
    print((e//16) + 1)