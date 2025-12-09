T=[int(input())]
Key=0
E=[1]
while len(T)!=0:
    if T[0]==2:
        T.pop(0)
        E.pop(0)
    elif T[0]==3:
        Key+=E[0]
        T.pop(0)
        E.pop(0)
    else:
        if T[0]%2==1:
            if T[0]//2+1 in T:
                E[T.index(T[0]//2+1)]+=E[0]
            else:
                T.append(T[0]//2+1)
                E.append(E[0])
            if T[0]//2 in T:
                E[T.index(T[0]//2)]+=E[0]
            else:            
                T.append(T[0]//2)
                E.append(E[0])        
        else:
            if T[0]//2 in T:
                E[T.index(T[0]//2)]+=E[0]*2
            else:            
                T.append(T[0]//2)
                E.append(E[0]*2)
        T.pop(0)
        E.pop(0)
print(Key)