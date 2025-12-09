a=input()
QWE=['a','b','c','d','e','f','g','h']
T=[]
e=[]   
y,x=int(a[1]),QWE.index(a[0])+1
T.append([x-2,y-1])
T.append([x-2,y+1])
T.append([x-1,y+2])
T.append([x-1,y-2])
T.append([x+1,y+2])
T.append([x+1,y-2])
T.append([x+2,y+1])
T.append([x+2,y-1])
for i in T:
    if min(i)>=1 and max(i)<=8 and i not in e:
        e.append(i)
for i in e:
    print(QWE[i[0]-1]+str(i[1]))