d,m,y=map(int,input().split('/'))
r=d+1
s=['0','1','2','3','4','5','6','7','8','9','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
d1,m1,y1='','',''
while d!=0:
    d1+=s[d%r]
    d//=r

while m!=0:
    m1+=s[m%r]
    m//=r

while y != 0:
    y1 += s[y % r ]
    y //= r
print(d1[::-1],m1[::-1],y1[::-1],sep='/')