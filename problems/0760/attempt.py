n,m,k =map(int,input().split())
if n>0:
    T=list(map(int,input().split()))
else:
    T=[0,0]
print('{0:.2f}'.format(sum(T[1::2])+k/m*60))