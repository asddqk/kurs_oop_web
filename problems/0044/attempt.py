p=input()
Oo=0
p=p + '0000'
for i in range (len(p)):
    if p[i] == '>' and p[i+1] =='>' and p[i+2] == '-' and p[i+3] == '-' and p[i+4] == '>' or p[i] == '<' and p[i+1] =='-' and p[i+2] == '-' and p[i+3] == '<' and p[i+4] == '<':  
        Oo+=1
print(Oo)