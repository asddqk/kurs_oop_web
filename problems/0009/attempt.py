z= int(input())
T=list(map(int, input().split()))
T1=[]
Chislo=1
e=0
Max=0
Min=0
for i in range(z):
    if T[i]>0:
        T1.append(T[i])
    if T[i]==max(T):
        Max=i+1
    if T[i]==min(T):
        Min=i+1  
if Max>Min:
    R=T[Min:Max-1]
else:
    R=T[Max:Min-1]
for i in range(len(R)):
    Chislo*=R[i]
print(sum(T1), Chislo)