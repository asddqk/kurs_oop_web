K=input()
R='qwertyuiopasdfghjklzxcvbnmq'
for i in range(100):
    if R[i]==K:
        print(R[i+1])
        break