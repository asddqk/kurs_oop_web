n=int(input())

for i in range (n) :
    f=0
    u=int(input())
    p=(u+1)
    p6= p%10
    p1 = p//100000
    p2 = (p//10000) % 10
    p3 = (p//1000) % 100 % 10
    p4 = (p%1000) // 100
    p5 = (p% 100) // 10
  #  print(p1,p2,p3,p4,p5,p6)
    if p1+p2+p3==p4+p5+p6:
        f=1
    p=(u-1)

    p6= p%10
    p1 = p//100000
    p2 = (p//10000) % 10
    p3 = (p//1000) % 100 % 10
    p4 = (p%1000) // 100
    p5 = (p% 100) // 10
   # print(p1,p2,p3,p4,p5,p6)
    if p1+p2+p3==p4+p5+p6:
        f=1    
    if f==1:
        print('Yes')
        
    else:
        print('No')