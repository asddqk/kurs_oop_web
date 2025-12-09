n=int(input())
T=[0]
T.extend(list(map(int, input().split())))
e=[0,T[1]]
i=2
p=[n]
while 1:
    try:
        e.append(max(e[i-1]+T[i],e[i-2]+T[i]))
    except:
        break
    i+=1
x=e[::-1][0]
print(x)
e=e[::-1]
i=0
while 1:
    if i>=n:
        break
    try:
        if e[i+1]<=e[i+2]:
            i+=2
            p.append(n-i)
        else:
            i+=1
            p.append(n-i)
    except:
        break
if 0 in p:
    p.pop(p.index(0))
print(*set(p))