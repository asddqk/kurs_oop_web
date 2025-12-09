n,m = map(int, input().split())
T1=[]
T2=[]
Key=[]
Alf=['q','a','z','x','s','w','e','d','c','v','f','r','t','g','b','n','h','y','u','j','m','k','i','o','l','p']
for i in range(n):
    T1.append(list(input()))
input()
for i in range(n):
    T2.append(list(input()))
for i in range(n):
    for l in range(m):
        if T1[i][l]!=T2[i][l]:
            if T2[i][l]=='.':
                pass
            else:
                Key.append(T2[i][l])            
print(len(Key))
t1=[]
t2=[]
for i in range(len(Key)):
    if Key[i] in Alf:
        t1.append(Key[i])
    else:
        t2.append(Key[i])
t1.sort()
t2.sort()
print(*t1,*t2,sep='')