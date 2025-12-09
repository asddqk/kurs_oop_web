n=int(input())
if n<10:
    v=[0]*10
    for i in range(0,n+1):
        if (str(i).replace('4','')).replace('7','')=='':
            v[len(str(i))]+=1
    print(sum(v))
else:
    r=1
    c=0
    while r<len(str(n)):
        c+=2**r
        r+=1
    chi=len(str(n))
    n=list(str(n))
    for tt in range(32):
        if n[0]=='0':
            n.pop(0)
        for i in range(len(n)):
            if int(n[i]) in [4,7]:
                if int(n[i])==4:
                    if i+1<len(n):
                        if n[i+1] in ['0','1','2','3']:
                            n[i]=str(int(n[i])-1)
                            for l in range(i+1,len(n)):
                                n[l]='9'
                else:
                    if i+1<len(n):
                        if n[i+1] in ['0','1','2','3']:
                            n[i]=str(int(n[i])-1)
                            for l in range(i+1,len(n)):
                                n[l]='9'          
            elif int(n[i]) in [5,6]:
                n[i]='4'
                for l in range(i+1,len(n)):
                    n[l]='7' 
            elif int(n[i]) in [8,9]:
                n[i]='7'
                for l in range(i+1,len(n)):
                    n[l]='7'   
            else:
                n[i]='0'
    if len(n)>=chi:
        k=2**chi
        for i in range(len(n)):
            if n[i]=='4':
                k-=2**(chi-i-1)
    else:
        k=0
    print(c+k )