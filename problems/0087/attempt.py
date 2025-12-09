T=[]
s=''
while s!='ENDOFINPUT':
    s=input()
    T.append(s)
T.pop(-1)
S=[]
for a in T:
    for b in T:
        if a+b in T:
            S.append(a+b)
print(sum(min(S.count(i),T.count(i),1) for i in T))