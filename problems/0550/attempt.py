n=int(input())
l=len(str(n))
if n%400==0 or (n%4==0 and n%100!=0):
    if l==4:
        print('12/09/'+str(n))
    if l==3:
        print('12/09/'+'0'+str(n))
    if l==2:
        print('12/09/'+'00'+str(n))
    if l==1:
        print('12/09/'+'000'+str(n))  
else:
    if l==4:
        print('13/09/'+str(n))
    if l==3:
        print('13/09/'+'0'+str(n))
    if l==2:
        print('13/09/'+'00'+str(n))
    if l==1:
        print('13/09/'+'000'+str(n))