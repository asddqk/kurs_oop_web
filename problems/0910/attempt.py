n,m=map(int,input().split())
t=2
s=0
for i in range(n):
    s+=t
    t=t*2*(i+2)
print(s%m)