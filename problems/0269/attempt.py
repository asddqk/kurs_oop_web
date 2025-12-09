a=input()
b=input()
f=a
g=b
M1=len(a)
M2=len(b)
if len(a)<=len(b):
    a += '0' * (len(b) - len(a))
else:
    b += '0' * (len(a) - len(b))
E=[]
for i in range(len(a)):
    E.append(int(a[i])+int(b[i]))
if max(E)<=3:
    print(len(a))
else:
    X=[]
    for i in range(101):
        a,b=f,g
        E=[]
        a='0'*i+a
        if len(a) <= len(b):
            a += '0' * (len(b) - len(a))
        else:
            b += '0' * (len(a) - len(b))
        for i in range(len(a)):
            E.append(int(a[i]) + int(b[i]))
        if max(E) <= 3:
            X.append(len(E))
    for i in range(101):
        a,b=f,g
        E=[]
        b='0'*i+b
        if len(a) <= len(b):
            a += '0' * (len(b) - len(a))
        else:
            b += '0' * (len(a) - len(b))
        for i in range(len(a)):
            E.append(int(a[i]) + int(b[i]))
        if max(E) <= 3:
            X.append(len(E))
    print(min(X))