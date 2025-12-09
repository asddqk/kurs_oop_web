n=input()
o=0
for i in range(len(n)):
    if n[i]=='0':
        o+=1
if o>=1:
    print('NO')
else:
    print('YES')