A,B,C,D= map(int, input().split())
F=''
for i in range(-101, 101 ):
    if A*(i**3) + B*i**2 + C*i + D==0:
        F+= str(i) + ' '
print(F)