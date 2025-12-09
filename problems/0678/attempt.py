D=input()
f=['win','lose','lose']
for i in range(len(D)):
    if D[i]=='A':
        f[0],f[1]=f[1],f[0]
    if D[i]=='B':
        f[2],f[1]=f[1],f[2]
    if D[i]=='C':
        f[0],f[2]=f[2],f[0]
if f[0]=='win':
    print('1')
if f[1]=='win':
    print('2')
if f[2]=='win':
    print('3')