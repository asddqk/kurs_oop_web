s=input()
x=1
T=[1]
for i in s:
    if i=='1':
        x+=1
    else:
        x-=1
    T.append(x)
if min(T)<=0:
    print(max(T)-min(T)+1)
else:
    if min(T)==1:
        print(max(T))
    else:
        print(max(T)-min(T)+1)