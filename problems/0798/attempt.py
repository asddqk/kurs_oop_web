m,n,c,v,b=map(int,input().split())
f=m%2
g=n%2
t=m//2
u=n//2
B=(t+f)*(u+g)+t*u
W=t*(u+g)+(t+f)*u
if (c+v)%2!=b or (c+v)%2!=b:
    B,W=W,B
print('equal' if B==W else ('black'  if B>W else 'white'))