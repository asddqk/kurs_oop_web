n=int(input())
k=0

for i in range(n):
    k=0
    s=input()
    if len(s)== 6 :
        if s[0]=='A' or s[0]=='B' or s[0]=='C' or s[0]=='E' or s[0]=='E' or s[0]=='H' or s[0]=='K' or s[0]=='M' or s[0]=='O' or s[0]=='P' or s[0]=='T' or s[0]=='X' or s[0]=='Y':
            k=k+1
        if ord(s[1])>47 and ord(s[1])<58:
            k=k+1
        if ord(s[2])>47 and ord(s[2])<58:
            k=k+1        
        if ord(s[3])>47 and ord(s[3])<58:
            k=k+1    
        if s[4]=='A' or s[4]=='B' or s[4]=='C' or s[4]=='E' or s[4]=='E' or s[4]=='H' or s[4]=='K' or s[4]=='M' or s[4]=='O' or s[4]=='P' or s[4]=='T' or s[4]=='X' or s[4]=='Y':
            k=k+1
        if s[5]=='A' or s[5]=='B' or s[5]=='C' or s[5]=='E' or s[5]=='E' or s[5]=='H' or s[5]=='K' or s[5]=='M' or s[5]=='O' or s[5]=='P' or s[5]=='T' or s[5]=='X' or s[5]=='Y':
            k=k+1
        if k==6:
            print('Yes')
        else:
            print('No')
    else:
        print('No')