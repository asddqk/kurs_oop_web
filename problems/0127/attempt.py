n=int(input())
T=[list(map(int, input().split())) for i in range(n)]
x,y=map(int, input().split())
e=[x-1]
s=[x-1]
c=0
while 1:
    if y-1 in e or len(e)==0:
        break
    Q=[]
    for i in e:
        for l in range(n):
            if T[i][l]==1:
                if l not in s:
                    s.append(l)
                    Q.append(l)
    e=Q
    c+=1
if len(e)==0:
    print(-1)
else:
    print(c)