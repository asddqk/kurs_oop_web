x= int(input())
S=1

while x>3:
    S+=1
    if x%3==1:
        x=(x+2)//3
    else:
        x=(x+1)//3
print(S)