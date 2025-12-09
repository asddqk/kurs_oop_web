n=input()
e=len(n)
T=[]
for i in range(e):
    R=0
    q=n[:i]+n[i+1:]
    for i in range(e-1):
        if i%2==0:
            R+=int(q[i])
        else:
            R-=int(q[i])
    T.append(R)
print(max(T))