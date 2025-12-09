X=int(input())
f=0
E=0
for i in range(X):
    for n in range(X):
        if X==5*i + 3*n:
            f=n
            E=i
            break
print(E , f)