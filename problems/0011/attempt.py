k,n=map(int, input().split())
T=[1]
for lo in range(n):
    S=0
    for i in range(k):
        if lo-i>=0:
            S+=T[lo-i]
    T.append(S)
print(T[n])