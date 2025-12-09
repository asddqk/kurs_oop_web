N=int(input())
S=0
for i in range (N):
    a=int(input())
    if a == 1:
        S=S+1
if S>N-S:
    print(N-S)
else:
    print(S)