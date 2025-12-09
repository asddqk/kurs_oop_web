T=[]
E=[]
_2=[]
for i in range(int(input())):
    T.append(input())
for i in range(int(input())):
    S=input()
    if S in T:
        E.append(S)
    else:
        _2.append(S)
T.sort()
E.sort()
_2.sort()
print('Friends: ',end='')
print(*T,sep=', ')
print('Mutual Friends: ',end='')
print(*E,sep=', ')
print('Also Friend of: ',end='')
print(*_2,sep=', ')