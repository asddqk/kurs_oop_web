n,m,k=map(int, input().split(':'))
n2,m2,k2=map(int, input().split(':'))
T=[0,0,0,0,0,0,0,0,0,0]

for i in str(n):
    T[int(i)]+=1
for i in str(m):
    T[int(i)]+=1
for i in str(k):
    T[int(i)]+=1
  
if n<10:
    T[0]+=1
if m<10:
    T[0]+=1
if k<10:
    T[0]+=1
while n*3600+m*60+k!=n2*3600+m2*60+k2:   
    k+=1
    if k>=60:
        m+=1
        k=0
    if m>=60:
        n+=1
        m=0
        k=0
              
    if n<10:
        T[0]+=1
    if m<10:
        T[0]+=1
    if k<10:
        T[0]+=1
                     
    for i in str(n):
        T[int(i)]+=1
    for i in str(m):
        T[int(i)]+=1
    for i in str(k):
        T[int(i)]+=1

print(*T,sep='\n')