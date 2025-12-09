poi = input()
E=1
Ron=str()
for i in range(len(poi)):
    if poi[i] == '0':
        E+=1
    if poi[i] == '1':
        Ron=Ron + chr(96+E)
        E=1
        
print(Ron)