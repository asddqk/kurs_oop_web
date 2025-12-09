a,b,c = map(int, input().split())
if a==0 and b==0 and c==0:
    print(-1)
else:
    if a==0 and b==0:
        print(0)
    else:
        if a==0:
            print(1)
            print(-c/b)  
        else:
            Di= b**2 -(4*a*c)
            if Di>0:
                XX= (-b + Di**0.5)/(2*a)
                X= (-b - Di**0.5)/(2*a)
                print(2)
                print(X)
                print(XX)
            if Di==0:
                XX= (-b + Di**0.5)/(2*a)
                print(1)
                print(XX)                
            if Di<0:
                print(0)