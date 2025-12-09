n,m,k=map(int, input().split())
F=93
G=728
if (n>F and n<G) and (m>F and m<G) and (k>F and k<G):
    print(max(n,m,k))
else:
    print('Error')