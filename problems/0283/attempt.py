n=input()
f=0
E=0
Rty=0
for i in range(len(n)):
    if ord(n[i])>=65 and ord(n[i])<=90:
        f+=1
        E=0
        if f==2:
            Rty=2
            break
    if ord(n[i])>=97 and ord(n[i])<=122:
        f=0
        E+=1
        if E>3:
            Rty=2
            break
if ord(n[len(n)-1])>=65 and ord(n[len(n)-1])<=90:
    Rty=2
if ord(n[0])>=97 and ord(n[0])<=122:
    Rty=2
if Rty==2:
    print('No')
else:
    print('Yes')