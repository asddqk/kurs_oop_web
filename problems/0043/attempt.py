n=input()
n=n+'1'
K=0
kmax=0

for i in range(len(n)):
    if n[i]=='0':
        K+=1
    else:
        if K>kmax:
            kmax=K  
        K=0

print(kmax)