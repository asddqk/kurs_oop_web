n= list(input())
z=[]
Q=0
true=[48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]
for i in range(len(n)):
    z.append(ord(n[i]))
    if ord(n[i]) not in true:
        Q+=1
        break
if Q==0:
    Z=max(z)
    if Z==48:
        print(2)
    else:
        if Z<=57:
            print(Z-47)
        else:
            print(Z-54)
else:
    print(-1)