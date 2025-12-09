input()
T=list(map(int,input().split()))
m=int(input())
e=list(map(int,input().split()))
for i in range(m):
    T[e[i]-1]-=1
for i in T:
    if i<0:
        print('yes')
    else:
        print('no')