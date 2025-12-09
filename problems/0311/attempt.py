n=int(input())
S=0
for i in range(1,n+1):
    E=1
    for l in range(1,i+1):
        E*=l
    S+=E
print(S)