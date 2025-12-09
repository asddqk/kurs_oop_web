U=input()
x=0
for i in range(1,len(U)):   
    t1=U[:i]
    t2=U[i:]
    l=0
    while int(t1)>=10:
        T1=0
        for l in range(len(t1)):
            T1+=int(t1[l])
        t1=str(T1)
    while int(t2)>=10:
        T2=0
        for l in range(len(t2)):
            T2+=int(t2[l])
        t2=str(T2) 
        T1=0
    if int(t2)==int(t1):
        x+=1
if x>0:
    print('YES')
else:
    print('NO')