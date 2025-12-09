n=int(input())
we=['0','1','2','3','4','5','6','7','8','9','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
for i in range(n):
    s=int(input())
    g=s
    f=[]
    f2=[]
    for d in range(2,37):
        s=g
        k=''
        while s!=0:
            k+=we[s%d]
            s//=d
        f.append(k[::-1])
        f2.append(len(set(k))+len(k))
    print(f2.index(min(f2))+2,f[f2.index(min(f2))])