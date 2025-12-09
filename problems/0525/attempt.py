T=[1]
for i in [1]*5**4:
    T+=[T[-1]+T[-1-(len(T)-1)//2]]
print(T[int(input())//2])