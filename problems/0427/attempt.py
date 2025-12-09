n=int(input())
T=[int(input()) for i in range(n)]
T=sorted(T)
s=T[0]
E=[i for i in range(1,s)]
if len(E)!=0:
    print(E[0])
else:
    for i in range(1,n):
        if T[i]<=s+1:
            s+=T[i]
        else:
            print(s+1)
            break
    else:
        print(s+1)