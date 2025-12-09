s = input()
t = input()
c = 0
i = 0
try:
    while 1:
        if t[i] == s[c]:
            c += 1
            i += 1
        else:
            i += 1
except:
    if c == len(s):
        print('YES')
    else:
        print('NO')