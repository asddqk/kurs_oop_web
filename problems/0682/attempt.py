n=int(input())
Min=10**(n-1)
Max=10**n-1
print((Max+Min)*(Max-Min)//2+(Max+1+Min)//2)