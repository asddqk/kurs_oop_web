g=input
n,m=map(int,g().split())
T=g()
print(len({T[i:i+m] for i in range(n-m+1)}))