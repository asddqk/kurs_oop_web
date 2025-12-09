L=input()
o=0
p=0
for i in range(4):
    if L[i] == L[i+5]:
        o+=1 
    if L[i] == L[5] or L[i] == L[6] or L[i] == L[7] or L[i] == L[8]:
        p+=1
print(o, p-o)