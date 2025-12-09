s=input()
x=int(input())
z=(s.replace('-',' ')).replace('+',' ')
z=z.split()
vv=[]
if s[0]!='-' and s[0]!='+':
    vv.append('+')
for i in s:
    if i in ['-','+']:
        vv.append(i)
Key=0
for i in range(len(z)):
    d=z[i]
    c=0
    for l in range(len(d)):
        if d[l]=='^':
            if d[l-1]=='x':
                if (x<0 and int(d[l+1])%2==0) or x>=0:
                    z[i]=d[:l-1]+str(abs(int(x))**int(d[l+1]))
                else:
                    z[i]=d[:l-1]+str(abs(int(x))**int(d[l+1]))
                    if vv[i]=='+':
                        vv[i]='-'
                    else:
                        vv[i]='+'                   
                c=1
                break
            else:
                a=d.split('^')
                if '*' in a[0]:
                    b=a[0].split('*')
                    z[i]=b[0]+'*'+str(int(b[1])**int(a[1]))
                else:
                    
                    z[i]=str(int(a[0])**int(a[1]))
                c=1
                break
    if c==0:
        z[i]=z[i].replace('x',str(x))

for i in range(len(z)):
    if '*' in z[i]:
        g=z[i].split('*')
        z[i]=int(g[0])*int(g[1])
    else:
        z[i]=int(z[i])
for i in range(len(vv)):
    Key+=int(int(str(vv[i])+'1')*int(z[i]))
print(int(Key))