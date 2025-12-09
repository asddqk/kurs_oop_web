e=[[0]*100 for i in range(100)]
n=int(input())
for trgf in range(n):
    d,f,g,h=map(int, input().split())
    for i in range(min(f,h),max(f,h)):
        for l in range(min(d,g),max(d,g)):
            e[i][l]+=1
c=0
d,f,g,h=map(int, input().split())
for i in range(min(f,h),max(f,h)):
    for l in range(min(d,g),max(d,g)):
        if e[i][l]>0:
            c+=e[i][l]
print(c)