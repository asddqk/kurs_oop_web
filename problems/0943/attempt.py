n,m,y,x= map(int,input().split())
c=0
z,yz,xz,v,yv,xv=0+m*2*c,1+2*c,1,2*m-1+m*2*c,2+2*c,1
for l in range(n*m+9):
    if yz==y and xz==x:
        print(z)
        break
    if yv==y and xv==x:
        print(v)
        break        
    if xz==m:
        z,yz,xz,v,yv,xv=0+m*2*c,1+2*c,1,2*m-1+m*2*c,2+2*c,1
        c+=1
    if yz==y and xz==x:
        print(z)
        break
    if yv==y and xv==x:
        print(v)
        break    
    z+=1
    xz+=1
    v-=1
    xv+=1