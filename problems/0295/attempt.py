R=input()
T=input()
ind1=R
ind2=''
Alf=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
zAlf=Alf[::-1]*2
for i in range(26):
    if T in ind1:
        print(ind1)
        break     
    for j in range(len(R)):
        for l in range(len(zAlf)):
            if ind1[j]==zAlf[l]:
                ind2+=zAlf[l+1]  
                break
    ind1=ind2
    ind2=''           
else:
    print('IMPOSSIBLE')