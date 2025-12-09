k,m=map(int,input().split())
T={}
for i in range(m):
    P,H=map(int,input().split())
    if H in T:
        T[H]+=[P]
    else:
        T[H] = [P]
T=dict(sorted(T.items())[::-1])
for i in T:
    if k in T[i]:
        k+=1
    else:
        if k-1 in T[i]:
            k-=1
print(k)