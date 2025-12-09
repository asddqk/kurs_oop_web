n,m=map(int,input().split())
e=[]
for i in range(n):
    c=0
    for l in input():
        if l=='.':
            c+=1
    e.append(c)
print(min(e))