n=input()
if n!=n[::-1]:
    print(n)
else:
    if len(n)==1:
        print('NO SOLUTION')
    else:
        n=n[1:]
        if n==n[::-1]:
            print('NO SOLUTION')
        else:
            print(n)