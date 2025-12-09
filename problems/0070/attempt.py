n=input()
k=int(input())
if k>0:
    if len(n)*k>1023:
        while len(n)*k>=1023:
            k-=1
        k+=1
        print((n*k)[:1023])
    else:
        print(n*k)
else:
    L=len(n)
    k=-k    
    if L%k!=0:
        print('NO SOLUTION')
    else:
        if n.replace(n[:L//k],'')=='':
            print(n[:L//k])
        else:
            print('NO SOLUTION')