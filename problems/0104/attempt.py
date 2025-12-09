from fnmatch import *
a=input()
b=input()
print("YES" if fnmatch(a,b) or fnmatch(b,a) else 'NO')