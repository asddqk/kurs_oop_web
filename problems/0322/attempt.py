Pr=''
N=input()
F=[1,2]
for i in range(21):
    F.append(F[i]+F[i+1])
i=0
while F[i]<=len(N):
    Pr+=N[F[i]-1]
    i+=1
print(Pr)