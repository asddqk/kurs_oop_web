n=int(input())
Max=10**3000+1
Min=0
while Min+10<Max:
    b=(Min+Max)//2
    if b*b<=n:
        Min=b-1
    else:
        Max=b+1
for i in range(Min,Max+1):
    if i*i>n:
        print(i-1)
        break