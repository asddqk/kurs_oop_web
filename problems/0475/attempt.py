T=[]
z=''
f = open('INPUT.TXT', 'r')
z=f.readline()
while len(z)!=0:
    T.extend(map(int, z.split()))
    z=f.readline()
T.sort()
e=0
for i in range(len(T)-2):
    if T[i+1]-T[i]!=T[i+2]-T[i+1]:
        e+=1
        break
if e==0:
    print('Yes')
else:
    print('No')
f.close()