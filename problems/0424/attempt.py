from functools import *
N=int(input())
@lru_cache(None)
def f(s,m):
    if s>=N:
        return m%2==0
    h=[f(s*i,m-1) for i in range(2,10)]
    return any(h) if (m-1)%2==0 else all(h)
print('Stan wins.' if f(1,1) else 'Ollie wins.')