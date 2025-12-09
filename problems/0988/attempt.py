for L in '0'*int(input()):
    k, p = map(int, input().split())
    r=1
    if p>2**6 or k<2**p:
        while k%2==0:
            r+=1
            k//=2
        print(r)
    else:
        print('No solution')