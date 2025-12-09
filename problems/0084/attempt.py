h,w=map(int, input().split())
e=[list(input()) for i in range(h)]
f=[]
y=[]
for i in range(h):
    for l in range(w):
        if e[i][l]=="*":
            y.append(i)
            f.append(l)
if len(f)!=0:
    for i in range(min(y),max(y)+1):
        for l in range(min(f),max(f)+1):
            e[i][l]="*"
for i in e:
    print(*i,sep='')