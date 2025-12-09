n=int(input())
T=list(map(int,input().split()))
E=[]
if n==1:
    print(0)
elif n==2:
    print(abs(T[0]-T[1]))
else:
    E.append(0)
    E.append(abs(T[0]-T[1]))
    for i in range(2,len(T)):
        E.append(min(min(3*abs(T[i]-T[i-2])+E[i-2],abs(T[i]-T[i-1])+E[i-1]),abs(T[i]-T[i-1])+E[i-1]))
    print(E[-1])