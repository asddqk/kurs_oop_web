s=input()
t=input()
f=len(s)
f2=len(t)
k=[]
k2=[]
s*=2
t*=2
for i in range(f):
    k.append(int(s[i:i+f]))
if int(t)==0:
    k2=[0]
else:
    for i in range(f2):
        if t[i:i+f2][0]!='0':
            k2.append(int(t[i:i+f2]))
print(max(k)-min(k2))