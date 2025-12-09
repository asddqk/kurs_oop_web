n,m=map(int, input().split(':'))
for hp in range(369852):
    m+=1
    if m==60:
        n+=1
        m=0
    if n==24:
        n=0
    if n<10:
        E='0'+str(n)
    else:
        E=str(n)
    if m<10:
        R='0'+str(m) 
    else:
        R=str(m)
    if E==R[::-1]:
        break
print(E,R,sep=':')