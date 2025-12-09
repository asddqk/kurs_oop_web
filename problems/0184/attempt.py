Key=0
T,E=[],[]
for i in 31,28,31,30,31,30,31,31,30,31,30,31,30:
    E.append([l+1 for l in range(i) ])
for j in range(int(input())):
    S,D=map(str, input().split())
    D=list(map(int, D.split(':')))
    G=0
    for x in range(int(S[3]+S[4])-1):
        G+=len(E[x])
    T.append([G+int(S[0]+S[1]) ,D[0],D[1]])
T.sort()
for j in range(0,len(T),2):
    v=T[j]
    c=T[j+1]
    if abs(v[0]-c[0])<=1:
        if abs(v[0]-c[0])==1:
            Key+=(c[1]*3600+c[2]*60-10*3600)+(18*3600-v[1]*3600-v[2]*60)+60
        else:
            Key+=(c[1]*3600+c[2]*60-(v[1]*3600+v[2]*60))+60    
    else:
        Key+=(c[0]-v[0]-1)*8*3600
        Key+=(c[1]*3600+c[2]*60-10*3600)+(18*3600-v[1]*3600-v[2]*60) +60   
if Key%3600//60<10:
    print(Key//3600,f'0{Key%3600//60}',sep=':')
else:
    print(Key//3600,Key%3600//60,sep=':')