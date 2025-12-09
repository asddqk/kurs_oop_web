f=[]
R=10
for hgi in range(5):
    x,y=map(int,input().split())
    h=[]
    for k in [0,0],[25,0],[50,0],[75,0],[100,0]:
        h.append(((k[0]-x)**2+(k[1]-y)**2)**0.5)
    for i in range(5):
        if h[i]<=R:
            f.append(i)
print(len(set(f)))