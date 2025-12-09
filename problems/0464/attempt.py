n=int(input())
S='0'
T=[]
for q in range(10):
    for i in range(len(S)):
        if S[i]=='0':
            S+='1'
        else:
            if S[i]=='1':
                S+='2'
            else:
                S+='0' 
for i in range(50):
    T.append(2**i)
Q=0
while n>1000:
    for i in range(len(T)-1):
        if n<T[i+1] and n>T[i]:
            n-=T[i]
            Q+=1
R=S[n-1]
for i in range(Q):
    if R=='0':
        R='1'
    else:
        if R=='1':
            R='2'
        else:
            R='0' 
print(R)