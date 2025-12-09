T=[list(map( str, input().split())) for i in range(5)]
a=0
G=[]
print(f'Ping statistics for {T[0][1]}:')
for i in range(1,5):
    if T[i]==['Time', 'out']:
        a+=1
    else:
        G.append(int((T[i][3].split('='))[1]))
print(f'Packets: Sent = {4} Received = {4-a} Lost = {a} ({int(a*100/4)}% loss)')
if a!=4:
    print('Approximate round trip times:')
    print(f'Minimum = {min(G)} Maximum = {max(G)} Average = {int(sum(G)/(4-a)+0.5)}')