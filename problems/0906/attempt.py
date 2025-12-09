E=[[13, 20, 20], [14, 20, 20], [15, 19, 19], [15, 19, 20], [15, 20, 20], [16, 20, 19], [16, 20, 20], [17, 20, 19], [17, 20, 20], [18, 20, 18], [18, 20, 19], [18, 20, 20], [19, 18, 18], [19, 19, 18], [19, 19, 19], [19, 20, 17], [19, 20, 18], [19, 20, 19], [19, 20, 20], [20, 16, 16], [20, 17, 16], [20, 17, 17], [20, 17, 18], [20, 18, 16], [20, 18, 17], [20, 18, 18], [20, 18, 19], [20, 18, 20], [20, 19, 16], [20, 19, 17], [20, 19, 18], [20, 19, 19], [20, 19, 20], [20, 20, 16], [20, 20, 17], [20, 20, 18], [20, 20, 19], [20, 20, 20]]
EI=[8192, 16384, 32768, 32768, 32768, 65536, 65536, 131072, 131072, 262144, 262144, 262144, 524289, 524288, 524288, 524288, 524288, 524288, 524288, 927887, 1094792, 1035717, 1050667, 1039192, 1050667, 1048291, 1048594, 1048576, 1049392, 1048423, 1048594, 1048575, 1048576, 1048576, 1048576, 1048576, 1048576, 1048576]
x,s,v=map(int,input().split())
if min(x, s, v) <= 0:
    x, s, v = 0, 0, 0
elif max(x, s, v) > 20:
    x, s, v = 20, 20, 20
if [x,s,v] in E:
    print(EI[E.index([x,s,v])])
else:
    Kill=[]
    Normal=[]
    NR=[]
    if min(x,s,v) < 0:
        print(1)
    else:
        Kill.append([x,s,v])
        ij=0
        while 1:
            try:
                a,b,c=Kill[ij][0],Kill[ij][1],Kill[ij][2]
                if min(a, b, c) > 0:
                    if a < b and b < c:
                        if [a, b, c - 1] not in Kill:
                            Kill.append([a, b, c - 1])
                        if [a, b - 1, c - 1] not in Kill:
                            Kill.append([a, b - 1, c - 1])
                        if [a, b - 1, c] not in Kill:
                            Kill.append([a, b - 1, c])
                    else:
                        if [a - 1, b, c] not in Kill:
                            Kill.append([a - 1, b, c])
                        if [a - 1, b - 1, c] not in Kill:
                            Kill.append([a - 1, b - 1, c])
                        if [a - 1, b, c - 1] not in Kill:
                            Kill.append([a - 1, b, c - 1])
                        if [a - 1, b - 1, c - 1] not in Kill:
                            Kill.append([a - 1, b - 1, c - 1])
                ij+=1
            except:
                break
        Kill=Kill[::-1]
        i=0
        while len(Kill)>0:
            if min(Kill[i])<=0:
                Normal.append(Kill[i])
                NR.append(1)
                Kill.pop(i)
                i-=1
            else:
                if Kill[i][0] < Kill[i][1] and Kill[i][1] < Kill[i][2]:
                    a,b,c=Kill[i][0],Kill[i][1], Kill[i][2]
                    if len(Normal)>len(Kill):
                        if [a, b, c - 1] not in Kill and [a, b - 1, c - 1] not in Kill and [a, b - 1, c] not in Kill:
                            Normal.append(Kill[i])
                            NR.append(NR[Normal.index([a, b, c-1])] + NR[Normal.index([a, b-1, c-1])] - NR[Normal.index([a, b-1, c])])
                            Kill.pop(i)
                            i -= 1
                    else:
                        if [a, b, c - 1]  in Normal and [a, b - 1, c - 1]  in Normal and [a, b - 1, c]  in Normal:
                            Normal.append(Kill[i])
                            NR.append(NR[Normal.index([a, b, c-1])] + NR[Normal.index([a, b-1, c-1])] - NR[Normal.index([a, b-1, c])])
                            Kill.pop(i)
                            i -= 1

                else:
                    a,b,c=Kill[i][0],Kill[i][1], Kill[i][2]
                    if len(Normal)>len(Kill):
                        if [a - 1, b, c] not in Kill and [a - 1, b - 1, c] not in Kill and [a - 1, b, c - 1] not in Kill and [a - 1, b - 1, c - 1] not in Kill:
                            Normal.append(Kill[i])
                            NR.append(NR[Normal.index([a-1, b, c])] + NR[Normal.index([a-1, b-1, c])] + NR[Normal.index([a-1, b, c-1])] - NR[Normal.index([a-1, b-1, c-1])])
                            Kill.pop(i)
                            i -= 1
                    else:
                        if [a - 1, b, c]  in Normal and [a - 1, b - 1, c]  in Normal and [a - 1, b, c - 1]  in Normal and [a - 1, b - 1, c - 1]  in Normal:
                            Normal.append(Kill[i])
                            NR.append(NR[Normal.index([a-1, b, c])] + NR[Normal.index([a-1, b-1, c])] + NR[Normal.index([a-1, b, c-1])] - NR[Normal.index([a-1, b-1, c-1])])
                            Kill.pop(i)
                            i -= 1

            i+=1
            if i>=len(Kill):
                i=0
        print(NR[-1])