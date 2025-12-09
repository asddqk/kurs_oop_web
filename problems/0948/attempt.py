n,m = map(int, input().split())
k=m%n
j=m//n
print(*(j+1,k) if k!=0 else (j, n))