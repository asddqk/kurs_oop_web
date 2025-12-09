j=input
j()
T = [int(i) for i in j().split()]
E = []
r=range
for i in r(len(T)): E.append(max([E[l] + 1 for l in r(i) if T[l] < T[i]] + [1]))
print(max(E))