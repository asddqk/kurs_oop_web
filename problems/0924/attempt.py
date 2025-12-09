R=[]
c=0
for i in range(4):
    r2=list(input())
    R.append(r2)
for i in range(3):
    for l in range(3):
        if R[i][l]==R[i+1][l]==R[i][l+1]==R[i+1][l+1]:
            c=1
            break
        else:
            c+=0
if c==0:
    print('Yes')
else:
    print('No')