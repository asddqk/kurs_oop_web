W=[input().split(' -> ') for i in range(int(input()))]
R=[]
for k in W:
    R.extend(k)
R=list(set(R))
n=len(R)
T=[[0]*n for i in range(n)]
e1=input()
e2=input()
if e1==e2:
    print(0)
else:
    try:
        x=R.index(e1)
        try:
            y=R.index(e2)
            e=[x]
            c=0
            for i in W:
                c1=R.index(i[0])
                c2=R.index(i[1])
                T[c1][c2]=1
            s=[x]
            while 1:   
                if y in e or len(e)==0:
                    break             
                Q=[]
                for i in e:
                    for l in range(n):
                        if T[i][l]==1:
                            if l not in s:
                                s.append(l)
                                Q.append(l)
                e=set(Q)
                c+=1    
            if len(e)==0:
                print(-1)
            else:
                print(c)
        except:
            print(-1)    
    except:
        print(-1)