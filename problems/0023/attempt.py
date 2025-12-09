X=int(input())
ER=0
for i in range(X):
    if X%(i+1)==0:
        ER+=(i+1)
print(ER)