t=int(input())
r=input().split()
e=0
opy=0
for i in range(t):
    if int(r[i])>0:
        e+=1
        if e>opy:
            opy=e     
    else:   
        e=0
print(opy)