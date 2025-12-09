q= int(input())
f=0
T=[]
for i in range(q):
    R=list(map(int, input().split()))
    T+= R[i:]
for i in range(len(T)):
    if T[i]==1:
        f+=1
print(f)