n = [int(i) for i in input()]
s = [int(i) for i in input()]
H = len(n) + len(s)
while len(n) < len(s) + 10:
    n.append(100)
while len(s) < len(n):
    s.append(100)
b = ''
Key = 0
while len(b) < H:

    if n[0] > s[0] or Key == 1 or n == s:
        b += str(s[0])
        s.pop(0)
        Key = 0
    elif n[0] < s[0] or Key == 2:
        b += str(n[0])
        n.pop(0)
        Key = 0
    else:
        while len(n) < len(s):
            n.append(100)
        while len(s) < len(n):
            s.append(100)
        for i in range(len(n)):
            if s[i] > n[i]:
                Key = 2
                break
            elif s[i] < n[i]:
                Key = 1
                break
            else:
                pass
print(b)