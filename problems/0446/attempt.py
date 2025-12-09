x,y = map(int, input().split())
T=[]
t=[]
for i in range(x*2):
    if i<x:
        T.append(input())
    else:
        t.append(list(map(int, input().split())))
c=0
def F(c):
    for i in range(x):
        for j in range(y):
            U=t[i][j]       
            if T[i][j] =='.':
                pass
            elif T[i][j] == 'R' and (U==4 or U==5 or U==6 or U==7):
                c+=1
            elif T[i][j] == 'G' and (U==2 or U==3 or U==6 or U==7):
                c+=1  
            elif T[i][j] == 'B' and (U==1 or U==3 or U==5 or U==7):
                c+=1        
            else:
                c=0
                return c
            
if F(c)==0:
    print('NO')
else:
    print('YES')