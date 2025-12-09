n,m,k = map(int, input().split())
T=[]
 
if m>1 and n>1:
    for i in range(n):
        R=[]
        for l in range(m):
            R.append('.')    
        T.append(R)
     
    for i in range(k):
        p,o=map(int, input().split())
        T[p-1][o-1]='*' 
    for i in range(1,n-1):
        for l in range(1,m-1):
            Key=0
            if T[i-1][l]=='*':
                Key+=1
            if T[i+1][l]=='*':
                Key+=1
            if T[i+1][l-1]=='*':
                Key+=1
            if T[i-1][l+1]=='*':
                Key+=1
            if T[i-1][l-1]=='*':
                Key+=1
            if T[i+1][l+1]=='*':
                Key+=1
            if T[i][l+1]=='*':
                Key+=1                               
            if T[i][l-1]=='*':
                Key+=1
            if T[i][l]=='.':
                if Key!=0:      
                    T[i][l]=Key
             
    for i in range(1,n-1):
        Key=0
        if T[i+1][0]=='*':
            Key+=1
        if T[i+1][1]=='*':
            Key+=1
        if T[i][1]=='*':
            Key+=1
        if T[i-1][1]=='*':
            Key+=1
        if T[i-1][0]=='*':
            Key+=1
        if T[i][0]=='.':
            if Key!=0:
                T[i][0]=Key
    for i in range(1,n-1):
        Key=0
        if T[i+1][m-1]=='*':
            Key+=1
        if T[i+1][m-2]=='*':
            Key+=1
        if T[i][m-2]=='*':
            Key+=1
        if T[i-1][m-2]=='*':
            Key+=1
        if T[i-1][m-1]=='*':
            Key+=1
        if T[i][m-1]=='.':
            if Key!=0:
                T[i][m-1]=Key  
    for i in range(1,m-1):
        Key=0
        if T[0][i+1]=='*':
            Key+=1
        if T[0][i-1]=='*':
            Key+=1
        if T[1][i-1]=='*':
            Key+=1
        if T[1][i+1]=='*':
            Key+=1
        if T[1][i]=='*':
            Key+=1
        if T[0][i]=='.':
            if Key!=0:
                T[0][i]=Key 
    for i in range(1,m-1):
        Key=0
        if T[n-1][i+1]=='*':
            Key+=1
        if T[n-1][i-1]=='*':
            Key+=1
        if T[n-2][i-1]=='*':
            Key+=1
        if T[n-2][i+1]=='*':
            Key+=1
        if T[n-2][i]=='*':
            Key+=1
        if T[n-1][i]=='.':
            if Key!=0:
                T[n-1][i]=Key 
    Key=0
    if T[0][1]=='*':
        Key+=1
    if T[1][0]=='*':
        Key+=1
    if T[1][1]=='*':
        Key+=1
    if T[0][0]=='.':
        if Key!=0:
            T[0][0]=Key
             
    Key=0
    if T[n-1][1]=='*':
        Key+=1
    if T[n-2][1]=='*':
        Key+=1
    if T[n-2][0]=='*':
        Key+=1
    if T[n-1][0]=='.':
        if Key!=0:
            T[n-1][0]=Key
             
    Key=0
    if T[0][m-2]=='*':
        Key+=1
    if T[1][m-1]=='*':
        Key+=1
    if T[1][m-2]=='*':
        Key+=1
    if T[0][m-1]=='.':
        if Key!=0:
            T[0][m-1]=Key
             
    Key=0
    if T[n-1][m-2]=='*':
        Key+=1
    if T[n-2][m-1]=='*':
        Key+=1
    if T[n-2][m-2]=='*':
        Key+=1
    if T[n-1][m-1]=='.':
        if Key!=0:
            T[n-1][m-1]=Key        
    for i in range(n):
        print(*T[i],sep='')
else:
    if m==1 and n!=1:
        for i in range(n):
            T.append('.')
        for i in range(k):
            p,o=map(int, input().split())
            T[p-1]='*'
        for i in range(1,n-1):
            Key=0
            if T[i-1]=='*':
                Key+=1
            if T[i+1]=='*':
                Key+=1
            if T[i]=='.':
                if Key!=0:
                    T[i]=Key
            if T[1]=='*' and T[0]=='.':
                T[0]=1
            if T[n-2]=='*' and T[n-1]=='.':
                T[n-1]=1           
        for i in range(n):
            print(T[i])
    else:
        if n==1 and m!=1:
            for i in range(m):
                T.append('.')
            for i in range(k):
                p,o=map(int, input().split())
                T[o-1]='*'
            for i in range(1,m-1):
                Key=0
                if T[i-1]=='*':
                    Key+=1
                if T[i+1]=='*':
                    Key+=1
                if T[i]=='.':
                    if Key!=0:
                        T[i]=Key
                if T[1]=='*' and T[0]=='.':
                    T[0]=1
                if T[m-2]=='*' and T[m-1]=='.':
                    T[m-1]=1           
            print(*T,sep='')
        else:
            if k==1:
                print('*')
            else:
                print('.')