try:
    S = input()

    Test = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '+', '=', '-', '*', '/']
    c = 0
    if '++' in S or '-+' in S or '/+' in S or '*+' in S or '=+' in S:
        rrr = 8 / 0
    for i in range(len(S)):
        if S[i] in Test:
            c += 1
    if len(S) == c:
        D = S.split('=')
        z = ''
        Key = '0'

        if D[0][0] == '-':
            z += '-'
            x = ''
            for i in range(1, len(D[0])):
                if D[0][i] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                    z += D[0][i]
                else:
                    x += D[0][i]
                    break
        else:
            z = ''
            x = ''
            for i in range(len(D[0])):
                if D[0][i] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                    z += D[0][i]
                else:
                    x += D[0][i]
                    break
        if x == '*':
            w = int(z) * int(D[0][len(z) + 1:])
        elif x == '/':
            if int(D[0][len(z) + 1:]) == 0:
                w = int(D[1]) + 1
            else:

                w = int(z) / int(D[0][len(z) + 1:])
        elif x == '-':
            w = int(z) - int(D[0][len(z) + 1:])
        else:
            w = int(z) + int(D[0][len(z) + 1:])
        if w == int(D[1]):
            print('YES')
        else:
            print('NO')
    else:
        print('ERROR')
except:
    print('ERROR')