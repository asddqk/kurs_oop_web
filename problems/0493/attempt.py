n,m = map(int, input().split())
List=[]
Rez=0
for i in range(n):
    List.append(list(input()))
 
for i in range(1,n-1):
    for l in range(1,m-1):
        if List[i][l]=='.' and List[i-1][l]=='.' and List[i+1][l]=='.' and List[i][l+1]=='.' and List[i][l-1]=='.':
            Rez+=1
if n>1 and m>1:
    for i in range(1,n-1):
            if (List[i][1]=='.' and List[i-1][0]=='.' and List[i+1][0]=='.' and List[i][0]=='.') :
                Rez+=1
            if (List[i][m-2]=='.' and List[i-1][m-1]=='.' and List[i][m-1]=='.' and List[i+1][m-1]=='.'):
                Rez+=1
    for i in range(1,m-1):
        if (List[1][i]=='.' and List[0][i-1]=='.' and List[0][i+1]=='.' and List[0][i]=='.'):
            Rez+=1
        if (List[n-1][i]=='.' and List[n-2][i]=='.' and List[n-1][i-1]=='.' and List[n-1][i+1]=='.'):
            Rez+=1
     
    if List[n-1][m-1]=='.' and List[n-2][m-1]=='.' and List[n-1][m-2]=='.':
        Rez+=1
    if List[0][0]=='.' and List[1][0]=='.' and List[0][1]=='.':
        Rez+=1
    if List[n-1][0]=='.' and List[n-1][1]=='.' and List[n-2][0]=='.':
        Rez+=1
    if List[0][m-1]=='.' and List[1][m-1]=='.' and List[0][m-2]=='.':
        Rez+=1
 
elif n==1 and m==1:
    if List[0][0]=='.':
        Rez+=1
elif n==1 and m!=1:
    for i in range(m-2):
        if '.' in [List[0][i-1],List[0][i],List[0][i+1]]:
            Rez+=1
    if '.' in [List[0][0],List[0][1]]:
        Rez+=1
    if '.' in [List[0][m-2],List[0][m-1]]:
        Rez+=1   
else:
    for i in range(n-2):
        if '.' in [List[i-1][0],List[i][0],List[i+1][0]]:
            Rez+=1 
    if '.' in [List[0][0],List[1][0]]:
            Rez+=1
    if '.' in [List[n-1][0],List[n-2][0]]:
            Rez+=1    
print(Rez)