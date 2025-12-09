n=int(input())
f=[]
while 1:
    f.append(n)
    g=list(str(n))
    g.sort()
    z=n
    n=''
    for i in g:
        if i!='-':
            n+=i
    n+='0'*(4-len(n))
    n=int(n[::-1])-int(n) 
    if n==z:
        break
print(n)
print(len(f)-1)