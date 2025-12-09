n=input()
T=0

for i in range(len(n)):
    if n[i]== '6' or n[i]=='9' or n[i]=='0':
        T+=1
    if n[i]== '8':
        T+=2
print(T)