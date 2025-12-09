E=int(input())
if E==0:
    print(3)
elif E==25:
    print('2.7182818284590452353602875')
else:
    E-=1
    N=7182818284590452353602875
    N=N//10**(23-E)
    if N%10>=5:
        N+=10
    N=str(N//10)
    print('2.' + N)