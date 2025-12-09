w = input()
N = {x: w.count(x) for x in ['N', 'S', 'W', 'E', 'U', 'D']}
w = input()
S = {x: w.count(x) for x in ['N', 'S', 'W', 'E', 'U', 'D']}
w = input()
W = {x: w.count(x) for x in ['N', 'S', 'W', 'E', 'U', 'D']}
w = input()
E = {x: w.count(x) for x in ['N', 'S', 'W', 'E', 'U', 'D']}
w = input()
U = {x: w.count(x) for x in ['N', 'S', 'W', 'E', 'U', 'D']}
w = input()
D = {x: w.count(x) for x in ['N', 'S', 'W', 'E', 'U', 'D']}

a, b = map(str, input().split())
C = 0
X = {'N': 0, 'S': 0, 'W': 0, 'E': 0, 'U': 0, 'D': 0}
X[a] += 1

for i in range(int(b) - 1):
    AQ = {'N': 0, 'S': 0, 'W': 0, 'E': 0, 'U': 0, 'D': 0}
    for l in X:
        for f in [N, S, W, E, U, D][['N', 'S', 'W', 'E', 'U', 'D'].index(l)]:
            AQ[f] += [N, S, W, E, U, D][['N', 'S', 'W', 'E', 'U', 'D'].index(l)][f] * X[l]
    X = AQ
    C += sum([X[l] for l in X])
print(C + 1)