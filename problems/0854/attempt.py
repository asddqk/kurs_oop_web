n,m = map(int, input().split())
E= input()
if E=='freeze':
    print(min(n,m))
elif E=='heat':
    print(max(n,m))
elif E=='auto':
    print(m)
else:
    print(n)