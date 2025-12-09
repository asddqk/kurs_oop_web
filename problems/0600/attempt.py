for i in range(int(input())):
    N=list(input())
    _0=0
    _1=0
    _2=0
    if N==sorted(N):
        for i in range(len(N)):
            if N[i]=='0':
                _0+=1
            if N[i]=='1':
                _1+=1
            if N[i]=='2':
                _2+=1
        if _0==_1==_2:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')