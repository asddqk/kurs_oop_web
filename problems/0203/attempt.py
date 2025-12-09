E=input()
R=input()
for i in range(len(E)):
    if E in R:
        print(i)
        break
    else:
        E=E[len(E)-1]+E[:len(E)-1]
else:
    print('-1')