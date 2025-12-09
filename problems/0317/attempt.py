x,y,z,n=map(int, input().split())
S=0
def F(S):
    for i in range(n//x + 1):
        N=n-x*i
        for ii in range(N//y + 1):
            if (N - y*ii)%z == 0:
                S+=1
    return S
print(F(S))