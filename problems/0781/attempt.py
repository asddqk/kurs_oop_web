n=int(input())
E=[2,4]
for i in range(32):
    E.append(E[i]+E[i+1])
print(E[n-1])