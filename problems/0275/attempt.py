n=int(input())
for i in range(n):
    ZET=0
    R=input()
    for i in range(len(R)):
        ZET+=int(R[i])*(2**(len(R)-(i+1))) 
    if ZET%7==0:
        print('Yes')
    else:
        print('No')