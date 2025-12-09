n=int(input())
T=[]
for i in range(n):
    E=int(input())
    for l in range(E):
        St=input()
        c,v=St.split()
        T.append([float(c),St])
T.sort(reverse=True)
print(len(T))
for i in range(len(T)):
    print(T[i][1])