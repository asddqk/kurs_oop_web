h=int(input())
e=[[0]*18 for i in range(18)]
deh=[[0]*18 for i in range(18)]
for i in range(h):
    x,y=map(int, input().split())
    e[x+2][y+2]="s"
for i in range(1,17):
    for l in range(1,17):
        if e[i][l]==0:
            g=0
            if e[i][l-1]=="s":
                g+=1
            if e[i][l+1]=="s":
                g+=1
            if e[i+1][l]=="s":
                g+=1
            if e[i-1][l]=="s":
                g+=1      
            deh[i][l]=g
g=0
for i in deh:
    g+=sum(i)       
print(g)