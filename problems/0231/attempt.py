N=input()
n=''
Ent=''
vvd=''
for i in range(len(N)):
    if ord(N[i]) >=48 and ord(N[i]) <=57:
        n= n + N[i]
    if ord(N[i]) >=65 and ord(N[i]) <=90:
        if n=='':
            Ent= Ent + (N[i])
        else:
            Ent = Ent + ((N[i])*int(n))
        n=''
for i in range(len(Ent)):
    if len(vvd) != 40:
        vvd= vvd +Ent[i]
    if len(vvd) == 40:
        print(vvd)
        vvd=''
print(vvd)