w,h=map(int, input().split())
e=[[0]*w for i in range(h)]
d=[list(input()) for i in range(h*2)]
y=input()
s=["00","01","10","11",y[0],y[1],y[2],y[3]]
for i in range(h):
    for l in range(w):
        z=d[i][l]+d[i+h][l]
        e[i][l]=s[s.index(z)+4]
for i in e:
    print(*i,sep='')