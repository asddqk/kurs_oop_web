n,m=map(int, input().split())
T=[6,28,496,8128,33550336,8589869056, 137438691328, 2305843008139952128]
k=0
for i in T:
    if i>=n and i<=m:
        print(i)
        k+=1
if k==0:
    print('Absent')