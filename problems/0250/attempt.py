n=int(input())
s1=n
s2=n
while len(set(list(str(s1))))>2:
    s1-=1
while len(set(list(str(s2))))>2:
    s2+=1
if abs(n-s1)<=abs(n-s2):
    print(s1)
else:
    print(s2)