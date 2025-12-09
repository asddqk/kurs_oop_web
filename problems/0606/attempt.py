N,M,c=map(int, input().split())
if N<M+c and M<N+c and c<N+M:
    print('YES')
else: 
    print('NO')