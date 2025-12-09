T=[0]*31
n=int(input())
for i in range(n):
    x,y=map(int,input().split())
    for l in range(x-1,y):
        T[l]+=1
print('YES' if max(T)==n else 'NO')