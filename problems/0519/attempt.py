n=input()
T=[]
N=list(map(int,str(n)))
N=sorted(N, reverse=True)
N2=sorted(N)
q=''
Q=''
for i in range(len(N)):
   if N[i]==0:
      q+='0'
   else:
      Q+=str(N[i]) 
T.append(Q+q)
q=''
Q=''
for i in range(len(N2)):
   if N2[i]==0:
      q+='0'
   else:
      Q+=str(N2[i])
T.append(Q[0]+q+Q[1:])
print(*sorted(T))