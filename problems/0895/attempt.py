T=[list(input()) for i in range(3)]
if (T[0][0]=='X' and T[0][1]=='X' and T[0][2]=='X') or (T[1][0]=='X' and T[1][1]=='X' and T[1][2]=='X') or (T[2][0]=='X' and T[2][1]=='X' and T[2][2]=='X') or (T[0][0]=='X' and T[1][0]=='X' and T[2][0]=='X') or(T[0][1]=='X' and T[1][1]=='X' and T[2][1]=='X') or (T[0][2]=='X' and T[1][2]=='X' and T[2][2]=='X') or (T[0][0]=='X' and T[1][1]=='X' and T[2][2]=='X') or (T[2][0]=='X' and T[1][1]=='X' and T[0][2]=='X'):
    print('Win')
elif (T[0][0]=='O' and T[0][1]=='O' and T[0][2]=='O') or (T[1][0]=='O' and T[1][1]=='O' and T[1][2]=='O') or (T[2][0]=='O' and T[2][1]=='O' and T[2][2]=='O') or (T[0][0]=='O' and T[1][0]=='O' and T[2][0]=='O') or(T[0][1]=='O' and T[1][1]=='O' and T[2][1]=='O') or (T[0][2]=='O' and T[1][2]=='O' and T[2][2]=='O') or (T[0][0]=='O' and T[1][1]=='O' and T[2][2]=='O') or (T[2][0]=='O' and T[1][1]=='O' and T[0][2]=='O'):
    print('Lose')
else:
    print('Draw')