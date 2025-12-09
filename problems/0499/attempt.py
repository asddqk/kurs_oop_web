K,W = map(int, input().split())
a,b,a2,b2,a3,b3 = map(int, input().split())
K,W=W,K
if (K-a>=0 and W-b<=0) or (K-a2>=0 and W-b2<=0) or (K-a3>=0 and W-b3<=0) or (K-a-a2>=0 and W-b-b2<=0) or (K-a3-a2>=0 and W-b3-b2<=0) or (K-a3-a>=0 and W-b3-b<=0) or (K-a-a2-a3>=0 and W-b-b2-b3<=0):
    print('YES')
else:
    print('NO')