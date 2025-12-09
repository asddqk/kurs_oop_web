n=int(input())
if n>=3:
    T=list(map(int, input().split()))
    e=sorted(T,reverse=True)
    a=e.pop(0)
    b=e.pop(0)
    key=0
    Max=0
    s=[0,0,0]
    while len(e)>0:
        for c in e:
            if a+b>c and a+c>b and c+b>a:
                key=1
                d = ((a + b + c) / 2)
                u = (d * (d - a) * (d - b) * (d - c)) ** 0.5
                if u>Max:
                    Max=u
                    s=[a,b,c]
        a,b=b,e.pop(0)
    if key==1:
        print("{:.10f}".format(Max))
        for i in range(n):
            if T[i] in s:
                print(i+1, end=' ')
                s.pop(s.index(T[i]))
            if len(s)==0:
                break
    else:
        print(-1)
else:
    print(-1)