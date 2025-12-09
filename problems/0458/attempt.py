n=int(input())
R=list(map(int, input().split()))
M=input()
T=[]
Rez=''
Zet=[]
if len(M)%n!=0:
    Dlinnaslova=len(M)//n+1
    Kolichestvo_celih_strok=len(M)%n
    Ostatok=n-Kolichestvo_celih_strok
    for l in range(Kolichestvo_celih_strok+1,n+1): 
        Zet.append(l)
    for i in range(n):
        if R[i] in Zet:
            M=M[:(i+1)*Dlinnaslova-1]+' '+M[(i+1)*Dlinnaslova-1:]
    
L=len(M)//n
i=0
for l in range(0,len(M),L):
    T.append([R[i],M[l:l+L]])
    i+=1    
T.sort()
for i in range(L):
    for l in range(n):
        if T[l][1][i]==' ':
            pass
        else:
            Rez+=T[l][1][i]      
print(Rez)