n=int(input())
T=list(map(int, input().split()))
if n%2==0:
    print(max(T[n//2],T[n//2-1]))
else:
    if n==1:
        print(*T)
    else:
        print(min(T[n//2],max(T[n//2+1],T[n//2-1])))