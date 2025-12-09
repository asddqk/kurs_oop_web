n=int(input())
T=list(map(int, input().split()))
e=[]
i=0
S=0
while 1:
    try:
        if len(e)>=10:
            e.append([T[i]])
            i += 1
        else:
            if T[i]==10:
                e.append([10])
                i+=1
            else:
                e.append([T[i],T[i+1]])
                i+=2
    except:
        break
for i in range(10):
    if e[i]==[10]:
        S+=10
        if len(e[i+1])==2:
            S+=sum(e[i+1])
        else:
            S+=sum(e[i+1])
            if len(e[i+2])==2:
                S += e[i + 2][0]
            else:
                S += sum(e[i + 2])
    elif sum(e[i])==10:
        if sum(e[i])==10:
            S+=10
            if len(e[i+1])==2:
                S += e[i + 1][0]
            else:
                S += sum(e[i + 1])
    else:
        S+=sum(e[i])
print(S)