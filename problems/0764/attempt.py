n=int(input())
a,b={0:0},{0:0}
R,T=0,0
for i in range(n):
    x,y=map(int,input().split())
    if x==0:
        if y>0:
            R+=1
        else:
            T+=1
    else:
        k = y / x
        if (x>0 and y>0) or (x<0 and y>0):
            if k in a:
                a[k]+=1
            else:
                a[k]=1
        else:
            if k in b:
                b[k]+=1
            else:
                b[k]=1
print(max(list(a.values())+list(b.values())+[R,T]))