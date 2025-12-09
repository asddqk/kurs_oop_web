N=input()
T=''
Dl=len(N)
KOD=0
Op=0
if N[0]=='_' or (ord(N[0])>=65 and ord(N[0])<=90) or N[Dl-1]=='_' :
    print('Error!')
else:
    for i in range(Dl):
        if N[i]=='_':
            KOD=9
            break
        else:
            KOD=6
        
    for i in range(Dl):
        if KOD==9 and ((ord(N[i])>=65 and ord(N[i])<=90)) or (N[i]=='_' and N[i+1]=='_'):
            print('Error!')
            Op=1
            break
   
           
    if KOD==6 and Op!=1:
        for i in range(Dl):
            if ord(N[i])>=97 and ord(N[i])<=122:
                T+=N[i]
            if ord(N[i])>=65 and ord(N[i])<=90 :
                T+='_'
                T+=chr(ord(N[i])+32)
    if KOD==9 and Op!=1:
        i=0
        while i!=Dl:
            if N[i]=='_':
                T+=chr(ord(N[i+1])-32)
                i+=1
            else:
                T+=N[i]
            i+=1
    if Op==0:
            print(T)