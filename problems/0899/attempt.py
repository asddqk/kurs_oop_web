f1=open('INPUT.TXT','r')
S=f1.readline()
for eeeee in range(12):
    v =0
    while v!=1:
        v=1
        i=0
        while i<len(S)-1:
            if (S[i] == '[' and S[i + 1] == ']') or (S[i] == '{' and S[i + 1] == '}') or (S[i] == '(' and S[i + 1] == ')'):
                S = S[:i]+ S[i + 2:]
                v = 0
                i=0
            i+=1
        if v==1:
            break
    if len(S) == 1:
        print(0,end='')
    else:
        print(1,end='')
    
    S=f1.readline()
    if S=='':
        break