j=int(input())
f=[]
f1=[]
for ji in range(j):
    sdf=input()
    for i in range(len(sdf)):
        if sdf[i]=='"':
            Key=i
    n=sdf[:Key+1]
    sdf=sdf[Key+1:]
    m,k=map(str, sdf.split())
    f.append(n)
    v, v1 = map(int, m.split(':'))
    b, b1 = map(int, k.split(':'))
    if v*60+v1>b*60+b1:
        z=24*60-abs(v*60+v1-b*60-b1)
    elif v*60+v1<b*60+b1:
        z = abs(v * 60 + v1 - b * 60 - b1)
    else:
        z=24*60
    f1.append(z)
print(f'The fastest train is {f[f1.index(min(f1))]}.')
s=min(f1)
t=650*60/s
print(f'Its speed is {int(t+0.5)} km/h, approximately.')