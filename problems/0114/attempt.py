n,k=map(int, input().split())
G=k-1
z=0
for kew in range(n-1):
    G,z=z*(k-1)+(G-z)*k,G-z
print(G)