n=int(input())
e=list(map(int,input().split()))
r=int(input())
G=[0]
for i in range(int(input())):
    d=0
    z=list(map(int,input().split()))
    for l in range(n):
        d+=e[l]*z[l]
    d-=2*i
    if sum(z)==n:
        d+=r
    B=max(max(G),d)
    G.append(B)
    print(B)