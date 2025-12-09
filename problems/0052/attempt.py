N=int(input())
n6=N%10
n1=N//100000
n2=N//10000-n1*10
n3=N//1000-n1*100-n2*10
n4=N%1000//100
n5=N%100//10

if n1+n2+n3==n4+n5+n6 :
    print('YES')
else:
    print('NO')