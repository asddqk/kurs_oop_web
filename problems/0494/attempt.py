x1, y1, x2, y2 = map(int, input().split())
if x2==x1:
    y1,y2,x1,x2=x1,x2,y1,y2
k = (y1 - y2) / (x1 - x2)
b = y1 - k * x1
R = 1
E = 0
for R in range(1,1415):
    H=k * k + 1
    D = 4 * k * k * b * b - 4 * H * (b * b - R * R)
    if D>0:
        D=D**0.5
    Q=-2*k*b
    mx=min(x1, x2)
    ax=max(x1, x2)
    if D>0:
        if mx <= ( Q + D ) / 2 / H <= ax:
            E += 1
        if mx <= ( Q - D ) / 2 / H <= ax:
            E += 1
    elif D==0:
        if mx <= Q / 2 / H <= ax:
            E += 1
print(E)