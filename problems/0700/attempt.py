n,v,k=map(int, input().split())
b=0
r=v
for i in range(n):
    if r>=0:
        b+=r
    r-=k
r+=k
print(f'{"YES" if r>0 else "NO"} {b}')