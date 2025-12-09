x=float(input())
f=0
for n in range(2,1000000000):
    if f>x:
        break
    else:
        f+=1/n
print(f'{n-2} card(s)')