a,b,c=map(int,input().split())
def F(x,y):
    S=''
    r=10
    while x+y>0:
        S=str(x%r+y%r)+S
        x//=r
        y//=r
    return int(S)
T=sorted({F(F(a,b),c),F(F(c,b),a),F(F(a,c),b)})
print(('NO' if len(T)==1 else 'YES'), *T,sep='\n')