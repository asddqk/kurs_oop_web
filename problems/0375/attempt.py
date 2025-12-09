n,m=map(int, input().split())
S=input()
E=['0','1','2','3','4','5','6','7','8','9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
S=S[::-1]
Sum=0
c=0
for i in S:
   Sum+=E.index(S[c])*(n**c) 
   c+=1
if Sum==0:
   print(0)
else:
   Q=''
   while Sum!=0:
      Q+=E[Sum%m]
      Sum//=m
   Q=Q[::-1]
   print(Q)