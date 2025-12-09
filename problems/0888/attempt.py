t=int(input())
r=list(map(int, input().split()))
Sum=0
R=0
for i in range(t):
    if r[i]==1:
        Sum= Sum + 3 + R
        R+=1
   # print(R,"R")
    if r[i]==0:
        Sum+=0
        R-=3
        if R<0:
            R=0
   # print(Sum,"S")
print(Sum)