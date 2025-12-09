n=input()
t=input().split()

for i in range (len(t)):
    t[i]=int(t[i])
print(min(t),max(t))