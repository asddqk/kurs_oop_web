a,b,c = map(int, input().split())
T=''
if a!=0:
    T+=str(a)

if b<0 and b!=0:
    if b==-1:
        T+='-x'
    else:
        T+=str(b)
        T+='x'
elif b>0 and b!=0:
    if b== 1:
        if a!=0:
            T+='+x'
        else:
            T+='x'
    else:
        if a!=0:
            T+='+'
            T+=str(b)
            T+='x' 
        else:
            T+=str(b)
            T+='x'            
if c<0 and c!=0:
    if c==-1:
        T+='-y'
    else:
        T+=str(c)
        T+='y'
elif c>0 and c!=0:
    if c== 1:
        if a!=0 or b!=0:    
            T+='+y'
        else:
            T+='y'
    else:
        if a!=0 or b!=0: 
            T+='+'
            T+=str(c)
            T+='y'
        else:
            T+=str(c)
            T+='y'            
if a==0 and b==0 and c==0:
    T+='0'
print(T)