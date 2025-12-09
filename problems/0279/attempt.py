s=input()
T = []
e = 0
try:
    for i in s:
        if i in '[(':
            T.append(i)
        else:
            if T[-1]+i in ['()','[]']:
                T.pop(-1)
            else:
                T.pop(-1)
                e+=1
    if len(T)!=0:
        e=0/0
    print(e)
except:
    print(-1)