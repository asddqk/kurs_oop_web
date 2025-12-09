primer=input()
if 'x' == primer[4]:
    if primer[1] == '-' :
        print(int(primer[0]) - int(primer[2]))
    else:
        print(int(primer[0]) + int(primer[2]))    
if 'x' == primer[0]:
    if primer[1] == '-' :
        print(int(primer[4]) + int(primer[2]))
    else:
        print(int(primer[4]) - int(primer[2]))

if 'x' == primer[2]:
    if primer[1] == '-' :
        print(-(int(primer[4]) - int(primer[0])))
    else:
        print(int(primer[4]) - int(primer[0]))