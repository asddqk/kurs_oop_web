n=int(input())
T=[]
for i in range(2,n+1):
    for l in range(1,i):
        z=i
        x=l
        while z!=0 and x!=0:
            if z>x:
                z%=x
            if z==0 or x==0:
                break
            if x>z:
                x%=z
            if z==0 or x==0:
                break 
        if max(z,x)==1:
            T.append([l/i,f'{l}/{i}'])
T.sort()

for i in T:
    print(i[1])