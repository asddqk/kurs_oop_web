E=int(input())
i=0
R=[1,1]


while E>R[i]:
    R.append(R[i]+R[i+1])
    i+=1
if E in R:
    print(1)
    print(i+1)
else:
    print(0)