a = int(input())
s = '0'+bin(a)[2:]
if s[-1]!='0':
    st=0
    for i in range(len(s)):
        if s[i]=='0':
            st=i
    q = s[:st] + '1' + '0' +s[st+2:]
    print(int(q,2))
else:
    st = 0
    for i in range(len(s)-1):
        if s[i]+s[i+1]=='01':
            st=i
    q = s[:st] + '1' + '0' + '0'*s[st + 2:].count('0')+'1'*s[st + 2:].count('1')
    print(int(q, 2))