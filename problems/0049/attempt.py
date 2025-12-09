S = input()
F = input()
y = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
k = ['a', 'b', 'c', 'd', 'e', 'f', 'g', '?']
D = [['0', '1', '2', '3'], ['1', '2', '3', '4'], ['2', '3', '4', '5'], ['3', '4', '5', '6'], ['4', '5', '6', '7'],
     ['5', '6', '7', '8'], ['6', '7', '8', '9'], y]
R = 1
for i in range(len(S)):
    if S[i] not in y:
        a = set(D[k.index(S[i])])
    else:
        a = {S[i]}

    if F[i] not in y:
        b = set(D[k.index(F[i])])
    else:
        b = {F[i]}
    R *= len(a & b)
print(R)