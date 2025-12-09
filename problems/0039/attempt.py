Len= int(input())
T= list(map(int, input().split()))
Rez=0
j=1
i=0
while i!=Len:
    if T[i]==max(T):
        Rez+=j*max(T)
        T=T[i+1:]
        Len=len(T)
        i=0
        j=0
    else:
        i+=1 
    j+=1 
print(Rez)