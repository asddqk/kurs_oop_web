n=int(input())
T=[1]
for lo in range(n):
    S=0
    for i in range(3):
        if lo-i>=0:
            S+=T[lo-i]
    T.append(S)
print(T[n])