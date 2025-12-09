n = int(input())
T=[]

for i in range(n):
    R=input().split()
    q=R[0]
    w=R[1]
    R[0]=int(R[0])
    if len(R[1])==1:
        if R[1]=='p':
            R[0]*=16380
        if R[1]=='t':
            R[0]*=1000000
    if len(R[1])==2:
        if R[1]=='mg':
            R[0]/=1000
        if R[1]=='kg':
            R[0]*=1000  
        if R[1]=='Mg':
            R[0]*=1000000
        if R[1]=='Gg':
            R[0]*=1000000000
        if R[1]=='mp':
            R[0]/=1000
            R[0]*=16380
        if R[1]=='kp':
            R[0]*=16380
            R[0]*=1000  
        if R[1]=='Mp':
            R[0]*=16380
            R[0]*=1000000
        if R[1]=='Gp':
            R[0]*=16380
            R[0]*=1000000000    
        if R[1]=='mt':
            R[0]*=1000000
            R[0]/=1000
        if R[1]=='kt':
            R[0]*=1000  
            R[0]*=1000000
        if R[1]=='Mt':
            R[0]*=1000000
            R[0]*=1000000
        if R[1]=='Gt':
            R[0]*=1000000000 
            R[0]*=1000000
    T.append([R[0],q,w])
for i in range(len(T)):
    for l in range(len(T)-1):
        if T[l][0]>T[l+1][0]:
            T[l],T[l+1]=T[l+1],T[l]
for i in range(len(T)):
    print(T[i][1],T[i][2])