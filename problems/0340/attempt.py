a,b,c=map(int, input().split())
a2,b2,c2=map(int, input().split())
U=[a,b,c]
U2=[a2,b2,c2]
U=sorted(U)
U2=sorted(U2)
if U==U2:
    print('Boxes are equal')
else:
    if U[0]<=U2[0] and U[1]<=U2[1] and U[2]<=U2[2]:
        print('The first box is smaller than the second one')
    elif U[0]>=U2[0] and U[1]>=U2[1] and U[2]>=U2[2]:
        print('The first box is larger than the second one')
    else:
        print('Boxes are incomparable')