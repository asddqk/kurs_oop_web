Rez=0
f1=open('INPUT.TXT','r')
n=f1.readline()
Alf=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
zAlf=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
Qwerty=['0','1','2','3','4','5','6','7','8','9']

while len(n)!=0:

    for i in range(len(n)):
        if n[i] in Alf:
            l=0
            for l in range(len(Alf)):
                if n[i]==Alf[l]:
                    l+=1
                    if l>=10:
                        Rez+=int(str(l)[0])+int(str(l)[1])
                    else:
                        Rez+=l
        if n[i] in zAlf:
            l=0
            for l in range(len(zAlf)):
                if n[i]==zAlf[l]:
                    l+=1
                    if l>=10:
                        Rez+=10+int(str(l)[0])+int(str(l)[1])
                    else:
                        Rez+=10+l
        if n[i]==' ':
            Rez+=4
        if n[i] in Qwerty:
            l=0
            for l in range(len(Qwerty)):
                if n[i]==Qwerty[l]:
                    Rez+=(13-int(Qwerty[l]))
        if n[i]=='.':
            Rez+=5   
        if n[i]==';':
            Rez+=7
        if n[i]==',':
            Rez+=2       
        if n[i]=='=':
            Rez+=3   
        if n[i]=='-':
            Rez+=3 
        if n[i]=='+':
            Rez+=3
        if n[i]=="'":
            Rez+=3       
        if n[i]=='"':
            Rez+=3  
        if n[i]==')':
            Rez+=1
        if n[i]=='(':
            Rez+=1 
        if n[i]=='>':
            Rez+=8 
        if n[i]=='<':
            Rez+=8
        if n[i]=='[':
            Rez+=8   
        if n[i]==']':
            Rez+=8  
        if n[i]=='}':
            Rez+=8
        if n[i]=='{':
            Rez+=8             
    n=f1.readline()
print(Rez)