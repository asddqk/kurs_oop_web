n,m = map(int, input().split(':'))
z,x = map(int, input().split())

Max=(n+z)*60+m+x
m=Max%60
n=Max//60
while  n>=24:
    n-=24
W=str(n)+':'+str(m)
if W[1]==':':
    W='0' + W
n,m = map(int, W.split(':'))
if m>=0 and m<=9:
    W=W[:3]+'0'+W[3]
print(W)