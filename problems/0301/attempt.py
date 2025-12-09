s,k=map(int,input().split())
MAX=''
s1=s
while len(MAX)!=k:
    if 0<s1<=9:
        MAX+=str(s1)
        s1=0
    elif s1>9:
        s1-=9
        MAX += '9'
    else:
        MAX+='0'
MIN=''
s1=s
while len(MIN)!=k:
    if len(MIN)==k-1:
        MIN = str(s1) + MIN
        s1=0
    elif 1<s1<=9:
        MIN = str(s1-1) + MIN
        s1=1
    elif s1>9:
        s1-=9
        MIN = '9' + MIN
    else:
        MIN='0' + MIN
print(MAX,MIN)