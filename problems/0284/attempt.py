X=int(input())
S=list(input().split())
E=int(input())
for i in range(E):
    C, C1=map(int, input().split())
    print(*S[(C-1):C1])