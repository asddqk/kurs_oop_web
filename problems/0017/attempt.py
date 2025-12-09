n=int(input())
T=input()
S=list(T.split())
S=S[:n-1]
T=T[:len(T)-len(S[0])]
for i in range(1,n-1):
    if S[0]==S[i] and (n-1)%i==0:
        w=T
        if len(w.replace(' '.join(S[:i]),'').replace(' ',''))==0:
            print(i)
            break
else:
    print(n-1)