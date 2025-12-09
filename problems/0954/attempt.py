t = [0] * 99
c=0
t[10] = t[11] = t[12] = 1
for i in range(int(input())):
    z=i-c
    t[z+10] += t[z]
    t[z + 11] +=  t[z]
    t[z + 12] +=  t[z]
    c+=1
    t.pop(0)
    t.append(0)
print(t[0]*2%10**6)