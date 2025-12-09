N=input()
Sp=['A','B','C','D','E','F','G','H']
SE=['1','2','3','4','5','6','7','8']
X=0
Y=0
x=0
y=0
if len(N)!=5:
    print('ERROR')
else:
    if N[0] in Sp and N[1] in SE and N[2]=='-' and N[3] in Sp and N[4] in SE:
        if N[0]=='A':
            X=1
        elif N[0]=='B':
            X=2
        elif N[0]=='C':
            X=3
        elif N[0]=='D':
            X=4
        elif N[0]=='E':
            X=5
        elif N[0]=='F':
            X=6
        elif N[0]=='G':
            X=7
        elif N[0]=='H':
            X=8
            
        Y=int(N[1])
        y=int(N[4])
        
        if N[3]=='A':
            x=1
        elif N[3]=='B':
            x=2
        elif N[3]=='C':
            x=3
        elif N[3]=='D':
            x=4
        elif N[3]=='E':
            x=5
        elif N[3]=='F':
            x=6
        elif N[3]=='G':
            x=7
        elif N[3]=='H':
            x=8
        if (X-x==2 and Y-y==1) or (X-x==-2 and Y-y==1) or (X-x==2 and Y-y==-1) or (X-x==-2 and Y-y==-1) or (X-x==1 and Y-y==2) or (X-x==-1 and Y-y==2) or (X-x==1 and Y-y==-2) or (X-x==-1 and Y-y==-2):
            print('YES')
        else:
            print('NO')        
    else:
        print('ERROR')