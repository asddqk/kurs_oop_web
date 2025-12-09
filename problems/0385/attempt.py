n=int(input())
T=[list(map(int,input().split())) for i in range(n)]
f=[]
for i in range(n):
    for l in range(i+1,n):
        x,y=T[i][0],T[i][1]
        xx, yy = T[l][0], T[l][1]
        s=(x-xx)**2+(y-yy)**2
        f.append(s**0.5)
print(len(set(f)))
print(*sorted(set(f)),sep='\n')