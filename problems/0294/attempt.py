a,b,c=map(int,input().split())
v,g,n=map(int,input().split())
s1=a//100*b
s2=v//100*g
a-=s1
v-=s2
if a>v:
    f=a-v
    f*=c
else:
    f=v-a
    f*=n    
print(s1*c+s2*n+f)