def R(t):
    if t==0:
        return 0
    if t==1:
        return 1
    else:
        return R(t-1) + R(t-2)
t=int(input())
print(R(t))