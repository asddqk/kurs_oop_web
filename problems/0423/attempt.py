from functools import *
@lru_cache(None)
def f(n):
    global g
    if len(n)>1:
        if n[0]+n[1] in g:
            return f(n[2:]) + f(n[1:])
        else:
            return f(n[1:])
    elif len(n)==1:
        return f(n[1:])
    else:
        return 1


n=input()
g = [str(i) for i in range(0,34)]
print(f(n))