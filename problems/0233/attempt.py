n=input()
t=input().split()
R=-1
for i in range (len(t)):
    t[i]=int(t[i])
    if t[i]<=437 and R==-1:
        R=i
if R==-1:
    print('No crash')
else:
    print('Crash',R+1)