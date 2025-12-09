n=int(input())-1
i=0
s=''
while n!=0:
    s+=str(n%3)
    n//=3
if s.count('2')%2==1:
    print(1)
else:
    print(0)