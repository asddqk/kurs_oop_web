n=int(input())
j=[]
T=list(map(int,input().split()))
T.sort()
for i in T:
    z=i
    if i%2==0:
        k=''
        while i!=0:
            k+=str(i%8)
            i//=8
        if k[2] in ['1','3','5','7','9']:
            j.append(z)
print(len(j))
print(*j)