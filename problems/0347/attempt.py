z,x,c,v,b=map(int, input().split())
T=[z,x,c,v,b]
E=[]
S=[]

for k in range(5):
    if T[k] not in E:
        E.append(T[k])
        S.append(1)
    else:
        S[E.index(T[k])]+=1
T.sort()
Pos=T[4]-T[3]
if max(S)==5:
    print("Impossible")
elif max(S)==4:
    print("Four of a Kind")
elif len(S)==2 and max(S)==3:
    print("Full House")
elif Pos==T[3]-T[2] and Pos==T[2]-T[1] and Pos==T[1]-T[0] and Pos==T[4]-T[3]:
    print("Straight")
elif len(S)==3 and max(S)==3:
    print("Three of a Kind")
elif len(S)==3 and max(S)==2:
    print('Two Pairs')
elif len(S)==4 and max(S)==2:
    print("One Pair")
else:
    print("Nothing")