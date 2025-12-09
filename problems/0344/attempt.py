n=int(input())
Q=list(map(int, input().split()))
T=sorted(Q)
m=T[1]-T[0]
m1=T[0]
m2=T[1]
for i in range(n-1):
    if T[i+1]-T[i]<m:
        m=T[i+1]-T[i]
        m1=T[i]
        m2=T[i+1]
for i in range(n):
    if Q[i]==m1:
        w1=i+1
    if Q[i]==m2:
        w2=i+1
print(m)
print(w1,w2)