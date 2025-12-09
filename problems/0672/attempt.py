d=[]

def F(s):
    T = []
    L = len(s)
    E = []
    Q = [0] * L
    for i in s:
        if i not in T:
            T.append(i)
        else:
            d = 0
            for l in range(len(E)):
                if E[l] == i:
                    Q[l] += 1
                    d = 1
            if d == 0:
                E.append(i)
                Q[len(E) - 1] += 1
    W = 1
    for i in range(L):
        W *= i + 1
    for l in range(len(Q)):
        d = 1
        for i in range(1, Q[l] + 1):
            d *= i + 1
        W //= d
    return W

n=int(input())
if n in [1,2,3]:
    print(*([[10, 0], [1, 22], [6, 123]][n-1]))
else:
    R=[]
    f=[]
    i= int('1'*n)

    while i<int('1'*n)+10000:
        T=[0]*10
        s=0
        s1=1
        for l in str(i):
            s+=int(l)
            T[int(l)]+=1
        for l in str(i):
            s1*=int(l)
        if s==s1:
            if T not in R:
                R.append(T)
            f.append(i)
        i+=1
    FG=0
    for i in R:
        k=''
        for l in range(10):
            k+=str(l)*i[l]
        FG+=F(k)
    d.append([FG,f[0]])
    print(*d[0])