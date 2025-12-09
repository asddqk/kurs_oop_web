s=int(input())
s-=1
if (s*10)//2+8*60<=20*60:
    print(((s*10)//2)//60,((s*10)//2)%60)
else:
    print('NO')