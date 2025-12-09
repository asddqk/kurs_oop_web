n= int(input())
L=''
while n//3!=0:
    L+=str(n%3)
    n=n//3
L+=str(n%3)
L=L[::-1]
for i in range(10):
    L=L.replace('10','03')
    L=L.replace('20','13')
    L=L.replace('30','23')
L=L.replace('0','')
print(L)